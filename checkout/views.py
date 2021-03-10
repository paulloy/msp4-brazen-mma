from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your bag is currently empty.')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ITVzDCznDimQa7lg9AIAVptqFeI2Ey5Jb2955Otdwtfj0Siftdmk2n7z169XTmB5SngNwcbdo68KJq13w25rEGm00UQD4e3zJ',
        'client_secret': 'test'
    }

    return render(request, template, context)
