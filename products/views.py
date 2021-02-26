from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from .models import Product, ProductSizesStock


def all_products(request):
    """ A view to return the index page """

    products = Product.objects.all()
    category = None
    product_type = None
    query = None

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

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # messages.error(
                #     request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'category': category,
        'product_type': product_type,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to return an individual products details """

    product = get_object_or_404(Product, pk=product_id)
    sizes = ProductSizesStock.objects.filter(product_id=product_id)
    save = None

    if product.rrp != product.price:
        save = product.rrp - product.price

    context = {
        'product': product,
        'sizes': sizes,
        'save': save,
    }

    return render(request, 'products/product_details.html', context)
