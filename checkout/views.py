from django.shortcuts import (render, redirect, reverse,
                              HttpResponse)
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from products.models import Product
from .forms import OrderForm
from .models import Order, OrderLineItem
from bag.contexts import bag_contents
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag')),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment\
             cannot be currently processed')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    test_if_bag_is_empty = request.session.get('bag', {})
    product_count = 0

    for product_id, product_data in test_if_bag_is_empty.items():
        for size, quantity in product_data['product_size'].items():
            product_count += quantity

    if product_count == 0:
        messages.error(request, 'You cannot checkout with an empty bag.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for product_id, item_data in bag.items():
                try:
                    product = Product.objects.get(product_id=product_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, qty in item_data['product_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=qty,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request, 'product does not exist in database.')
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'there was an error')

    else:
        current_bag = bag_contents(request)
        total = current_bag['total'] + settings.DEFAULT_DELIVERY_CHARGE
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.default_email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ Handle successful checkouts """
    save_info = request.session.get('save_info')

    try:
        order = Order.objects.get(order_number=order_number)
    except Exception:
        messages.error(request, 'Order does not exist.')
        return redirect(reverse('home'))

    if not request.user.is_anonymous:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()
    else:
        order.user_profile = None

    if save_info:
        profile_data = {
            'default_full_name': order.full_name,
            'default_email': order.email,
            'default_phone_number': order.phone_number,
            'default_country': order.country,
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_county': order.county,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(
        request, f'Order successful, Your order number is {order_number}')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'

    context = {
        'order': order,
    }

    return render(request, template, context)
