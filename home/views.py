from django.shortcuts import render

from products.views import Product

import random


def index(request):
    """ A view to return the index page """

    products = Product.objects.all()

    products_bjj = random.sample(
        list(products.filter(category__contains='bjj')), 8)
    products_mma = random.sample(
        list(products.filter(category__contains='mma')), 8)
    products_muay_thai = random.sample(
        list(products.filter(category__contains='muay thai')), 8)

    context = {
        'products_bjj': products_bjj,
        'products_mma': products_mma,
        'products_muay_thai': products_muay_thai,
    }

    return render(request, 'home/index.html', context)
