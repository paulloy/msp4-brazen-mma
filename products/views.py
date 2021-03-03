from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from .models import Product, ProductSizesStock


def all_products(request):
    """ A view to return the index page """

    products = Product.objects.all()
    category = None
    product_type = None
    query = None
    sort = None
    direction = None
    current_sorting = None

    if request.GET:

        if 'category' and 'product_type' in request.GET:
            category = request.GET['category']
            product_type = request.GET['product_type']
            products = products.filter(category__contains=category)
            products = products.filter(
                product_type__contains=product_type)
        elif 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__contains=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # messages.error(
                #     request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) \
                | Q(category__icontains=query) \
                | Q(product_type__icontains=query)
            products = products.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            current_sorting = f'{sort} {direction}'

    context = {
        'products': products,
        'category': category,
        'product_type': product_type,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to return an individual products details """

    product = get_object_or_404(Product, pk=product_id)
    sizes = ProductSizesStock.objects.filter(product_id=product_id)
    save = None

    if product.rrp != product.price:
        save = product.rrp - product.price

    low_stock = False
    no_stock = False

    for size in sizes:
        if size.stock == 0:
            no_stock = True
        elif 0 < size.stock <= 5:
            low_stock = True

    context = {
        'product': product,
        'sizes': sizes,
        'save': save,
        'low_stock': low_stock,
        'no_stock': no_stock
    }

    return render(request, 'products/product_details.html', context)
