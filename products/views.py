from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.forms.models import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers

from .models import Product, ProductSizesStock
from .forms import ProductForm, ProductSizesStockForm

import random


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
            
            if filters == 'DISCOUNTED':
                products = products.filter(sale__exact=True)
            else:
                products = products.filter(
                    Q(gender__iexact=filters) | Q(gender__iexact='UNISEX'))

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
    has_sizes = True

    for size in sizes:
        if size.stock == 0:
            no_stock = True
        elif 0 < size.stock <= 5:
            low_stock = True

        if size.size == 'false':
            has_sizes = False

    context = {
        'product': product,
        'sizes': sizes,
        'save': save,
        'low_stock': low_stock,
        'no_stock': no_stock,
        'has_sizes': has_sizes,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):

    if not request.user.is_superuser:
        messages.error(request, 'sorry this page is private')
        return redirect(reverse('home'))

    ProductSizesStockFormSet = inlineformset_factory(
        Product, ProductSizesStock, ProductSizesStockForm, extra=5)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        product = form.save()

        if form.is_valid():
            formset = ProductSizesStockFormSet(request.POST, instance=product)

            if formset.is_valid():
                formset.save()

                messages.success(request, 'product added')
                return redirect('add_product')
            else:
                messages.error(request, 'product failed to add')

        else:
            messages.error(request, 'product failed to add')
    else:
        form = ProductForm()
        formset = ProductSizesStockFormSet()

    template = 'products/add_product.html'

    context = {
        'form': form,
        'formset': formset,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, 'sorry this page is private')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    ProductSizesStockFormSet = inlineformset_factory(
        Product, ProductSizesStock, ProductSizesStockForm, extra=2)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            formset = ProductSizesStockFormSet(request.POST, instance=product)

            if formset.is_valid():
                formset.save()
                messages.success(
                    request, f'{product.name} successfully updated')
                return redirect(reverse(
                    'product_details', args=[product.product_id]))
            else:
                messages.error(request, f'Failed to update {product.name}')
        else:
            messages.error(request, f'Failed to update {product.name}')
    else:
        form = ProductForm(instance=product)
        formset = ProductSizesStockFormSet(instance=product)
        messages.info(request, f'You are currently editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'formset': formset,
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


def ajax_q_request(request):

    all_products = Product.objects.all()
    product_preview = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']

            queries = Q(name__icontains=query) \
                | Q(category__icontains=query) \
                | Q(product_type__icontains=query)
            products = all_products.filter(queries)

            if len(products) > 4:
                products = random.sample(list(products), 4)

            product_preview = serializers.serialize("json", products)

    return JsonResponse(product_preview, safe=False)
