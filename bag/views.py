from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from products.views import Product
from django.shortcuts import get_object_or_404


def view_bag(request):
    """ A view to return the bag template """

    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add a product to the bag with its quantity """

    """
        If a user accesses this function by url,
        redirect them to the home page
    """
    try:
        product = Product.objects.get(pk=product_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
    except Exception:
        messages.error(request, '403 Forbidden')
        return redirect(reverse('home'))

    size = request.POST['size']
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        if size in bag[product_id]['product_size'].keys():
            bag[product_id]['product_size'][size] += quantity
        else:
            bag[product_id]['product_size'][size] = quantity
    else:
        bag[product_id] = {'product_size': {size: quantity}}

    request.session['bag'] = bag

    if size == 'false':
        messages.success(
            request, f'<strong>{product.name}</strong> | added to bag.')
    else:
        messages.success(
            request, f'<strong>{product.name}</strong> | Size: <strong>{size}</strong>\
                 | added to bag.')

    return redirect(redirect_url)


def adjust_bag(request, product_id):
    """ update quantity of products in bag """

    product = get_object_or_404(Product, pk=product_id)
    bag = request.session.get('bag', {})

    """ Check that the product exists in bag """
    try:
        bag[product_id]
    except Exception:
        messages.error(request, '403 Forbidden')
        return redirect(reverse('home'))

    """ Check that quantity is of type 'int' """
    try:
        quantity = int(request.POST.get('quantity'))
    except Exception:
        messages.error(
            request, 'Bad request: Input must be an integer.')
        return redirect(reverse('view_bag'))

    size = request.POST['size']

    bag[product_id]['product_size'][size] = quantity

    request.session['bag'] = bag

    if size == 'false':
        messages.success(
            request, f'<strong>{product.name}</strong> | quantity updated.')
    else:
        messages.success(
            request, f'<strong>{product.name}</strong> | Size: \
                <strong>{size}</strong> | quantity updated.')

    return redirect(reverse('view_bag'))


def remove_from_bag(request, product_id):
    """ Remove product from bag """

    """
        If a user accesses this function by url,
        redirect them to the home page
    """
    try:
        product = Product.objects.get(pk=product_id)
        bag = request.session.get('bag', {})
        size = request.POST['size']
    except Exception:
        messages.error(request, '403 Forbidden.')
        return redirect(reverse('home'))

    """ Try delete bag item. Return error if item does not exist """
    try:
        del bag[product_id]['product_size'][size]
    except Exception:
        messages.error(
            request, 'Product cannot be removed. \
                Product does not exist in bag.')
        return redirect(reverse('view_bag'))

    if size == 'false':
        messages.success(
            request, f'<strong>{product.name}</strong> | removed from bag.')
    else:
        messages.success(
            request, f'<strong>{product.name}</strong> | Size: <strong>\
                {size}</strong> | removed from bag.')

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))
