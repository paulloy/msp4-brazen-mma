from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Product


class TestModels(TestCase):

    def test_order_model(self):
        """ create order """
        order = Order.objects.create(full_name='testy mctest')

        """ test model string """
        self.assertEqual(str(order), order.order_number)

    def test_orderlineitem_model(self):
        """ create order """
        order = Order.objects.create(full_name='testy mctest')

        """ create product """
        product = Product.objects.create(name='test', rrp=1.00, price=1.00)

        """
            create order_line_item with product_id
            and order.id as foreign keys
         """
        order_line_item = OrderLineItem.objects.create(
            product=product, order_id=order.id)

        """ test model string """
        self.assertEqual(str(order_line_item), (
            f'{order_line_item.product.product_id} in order ' +
            f'{order_line_item.order.order_number}'))

        """ Delete order_line_item """
        order_line_item.delete()
