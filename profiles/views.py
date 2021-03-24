from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib.auth.decorators import login_required


@login_required
def profile_delivery_info(request):
    """ Display user delivery information """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Default delivery information updated successfully.')

    form = UserProfileForm(instance=profile)

    template = 'profiles/delivery-info.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def profile_order_history(request):
    """ Display user order history """

    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    template = 'profiles/order-history.html'

    context = {
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order {order_number}'))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
