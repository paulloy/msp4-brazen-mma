from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    delivery_charge = settings.DEFAULT_DELIVERY_CHARGE

    for product_id, product_data in bag.items():
        if isinstance(product_data, int):
            product = get_object_or_404(Product, pk=product_id)
            total += product_data * product.price
            product_count += product_data
            bag_items.append({
                'product_id': product_id,
                'quantity': product_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=product_id)
            for size, quantity in product_data['product_size'].items():
                total += quantity * product.price
                product_count += quantity

                bag_items.append({
                    'product_id': product_id,
                    'quantity': product_data,
                    'product': product,
                    'size': size,
                    'qty': quantity
                })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery_charge': delivery_charge,
        'grand_total': total + delivery_charge,
    }

    return context
