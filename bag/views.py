from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from products.views import Product


def view_bag(request):
    """ A view to return the bag template """

    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add a product to the bag with its quantity """

    product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'size' in request.POST:
        size = request.POST['size']
    bag = request.session.get('bag', {})

    if size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['product_size'].keys():
                bag[product_id]['product_size'][size] += quantity
            else:
                bag[product_id]['product_size'][size] = quantity
        else:
            bag[product_id] = {'product_size': {size: quantity}}

    elif size == 'false':
        if product_id in list(bag.keys()):
            bag[product_id] += quantity
        else:
            bag[product_id] = quantity

    request.session['bag'] = bag

    messages.success(request, f'{product.name} | {size} added to bag.')

    return redirect(redirect_url)


def adjust_bag(request, product_id):
    """ update quantity of products in bag """

    product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'size' in request.POST:
        size = request.POST['size']
    bag = request.session.get('bag', {})

    if size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['product_size'].keys():
                bag[product_id]['product_size'][size] = quantity
        else:
            bag[product_id] = {'product_size': {size: quantity}}

    request.session['bag'] = bag

    messages.success(request, f'{product.name} | {size} quantity adjusted.')

    return redirect(reverse('view_bag'))


def remove_from_bag(request, product_id):
    """ Remove product from bag """

    bag = request.session.get('bag', {})
    size = request.POST['size']

    del bag[product_id]['product_size'][size]

    if not bag[product_id]['product_size']:
        bag.pop(product_id)

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))

