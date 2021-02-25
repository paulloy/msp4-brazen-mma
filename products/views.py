from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ A view to return the index page """

    products = Product.objects.all()
    category = None
    product_type = None

    if request.GET:
        if 'category' and 'product_type' in request.GET:
            category = request.GET['category']
            product_type = request.GET['product_type']
            products = products.filter(category__name__contains=category)
            products = products.filter(
                product_type__name__contains=product_type)
        elif 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name__contains=category)

    context = {
        'products': products,
        'category': category,
        'product_type': product_type,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to return an individual products details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
