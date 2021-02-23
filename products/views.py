from django.shortcuts import render


def all_products(request):
    """ A view to return the index page """

    return render(request, 'products/products.html')
