from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
import random
from products.views import Product


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def ajax_request(request):

    all_products = Product.objects.all()
    product_preview = None

    if request.GET:
        category = request.GET['category']
        product_type = request.GET['product_type']

        product_preview = all_products.filter(category__contains=category)
        product_preview = product_preview.filter(
            product_type__contains=product_type)
        product_preview = random.sample(list(product_preview), 4)

        product_preview = serializers.serialize("json", product_preview)

    return JsonResponse(product_preview, safe=False)
