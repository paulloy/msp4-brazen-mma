from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from .models import Product, ProductSizesStock
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def all_products(request):
    """ A view to return the index page """

    products = Product.objects.all()
    category = None
    product_type = None
    query = None
    sort = None
    direction = None
    filters = None

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

        if 'filters' in request.GET:
            filters = request.GET['filters']
            if filters == 'MEN' or 'WOMEN':
                products = products.filter(
                    Q(gender__iexact=filters) | Q(gender__iexact='UNISEX'))
            else:
                products = products.filter(gender__iexact=filters)

    context = {
        'products': products,
        'category': category,
        'product_type': product_type,
        'search_term': query,
        'sort': sort,
        'direction': direction,
        'filters': filters,
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


@login_required
def add_product(request):

    if not request.user.is_superuser:
        messages.error(request, 'sorry this page is private')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'product added')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'product failed to add')
    else:
        form = ProductForm()

    template = 'products/add_product.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, 'sorry this page is private')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'product updated')
            return redirect(reverse(
                'product_details', args=[product.product_id]))
        else:
            messages.error(request, 'failed to update product')
    else:
        form = ProductForm(instance=product)
        messages.info(request, 'You are editing a product')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, 'sorry this page is private')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products'))
