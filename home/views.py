from django.shortcuts import render

from products.views import Product

import random


def index(request):
    """ A view to return the index page """

    try:
        products = Product.objects.all()

        products_bjj = random.sample(
            list(products.filter(category__contains='bjj')), 6)
        products_mma = random.sample(
            list(products.filter(category__contains='mma')), 6)
        products_muay_thai = random.sample(
            list(products.filter(category__contains='muay thai')), 6)
    except Exception:
        products_bjj = None
        products_mma = None
        products_muay_thai = None

    context = {
        'products_bjj': products_bjj,
        'products_mma': products_mma,
        'products_muay_thai': products_muay_thai,
    }

    return render(request, 'home/index.html', context)
