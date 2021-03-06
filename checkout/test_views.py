from django.test import TestCase
from products.models import Product


class TestViews(TestCase):

    def test_checkout_view(self):
        """ create product """
        product = Product.objects.create(
            name='test add to bag', price=0.00, rrp=0.00)

        """ add product to bag """
        self.client.post(f'/bag/add/{product.product_id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.product_id}/',
            'size': 'test size',
        })

        """ test that view is rendered """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_view_empty_bag_redirect(self):
        """ test redirect when bag is empty """
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/')
