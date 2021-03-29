from django.test import TestCase
from products.models import Product


class TestViews(TestCase):
    """ test bag/views.py """

    def test_bag_view(self):
        """
            Test that view_bag() returns with a status code
            of 200, and the correct template rendered.
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):
        """ Create a test product """
        product = Product.objects.create(
            name='test add to bag', price=0.00, rrp=0.00)

        """ Add test product to bag """
        response = self.client.post(f'/bag/add/{product.product_id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.product_id}/',
            'size': 'L',
        })

        """ test that user is redirected to correct view """
        self.assertRedirects(response, f'/products/{product.product_id}/')

    def test_add_to_bag_size_false(self):
        """ Create a test product """
        product = Product.objects.create(
            name='test add to bag', price=0.00, rrp=0.00)

        """ Add test product to bag with size 'false' """
        response = self.client.post(f'/bag/add/{product.product_id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.product_id}/',
            'size': 'false',
        })
        self.assertRedirects(response, f'/products/{product.product_id}/')

    def test_add_to_bag_exception(self):
        """
            Test that user is redirected if add_to_bag()
            is called by URL with an invalid product_id
        """
        response = self.client.get('/bag/add/invalid_id/')
        self.assertRedirects(response, '/')

    def test_if_size_in_bag_is_same(self):
        """ Create a test product """
        product = Product.objects.create(
            name='test add to bag', price=0.00, rrp=0.00)

        """ Add product to bag """
        self.client.post(f'/bag/add/{product.product_id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.product_id}/',
            'size': 'test size',
        })

        """ Add product to bag again """
        response = self.client.post(f'/bag/add/{product.product_id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.product_id}/',
            'size': 'test size',
        })

        """ test that user is redirected to correct view """
        self.assertRedirects(response, f'/products/{product.product_id}/')

    def test_if_size_in_bag_is_different(self):
        """ Create a test product """
        product = Product.objects.create(
            name='test add to bag', price=0.00, rrp=0.00)

        """ Add product to bag of size 'test size 1' """
        self.client.post(f'/bag/add/{product.product_id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.product_id}/',
            'size': 'test size 1',
        })

        """ Add the same product to bag but with size 'test size 2' """
        response = self.client.post(f'/bag/add/{product.product_id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.product_id}/',
            'size': 'test size 2',
        })

        """ test that user is redirected to correct view """
        self.assertRedirects(response, f'/products/{product.product_id}/')

    def test_adjust_bag(self):
        """ Create a test product """
        product = Product.objects.create(
            name='test adjust bag', price=0.00, rrp=0.00)

        """ Add product to bag """
        self.client.post(f'/bag/add/{product.product_id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.product_id}/',
            'size': 'test',
        })

        """ adjust quantity of product in bag """
        response = self.client.post(f'/bag/adjust/{product.product_id}/', {
            'quantity': 5,
            'size': 'test',
        })
        self.assertRedirects(response, '/bag/')

    def test_adjust_bag_size_false(self):
        """ Create a test product """
        product = Product.objects.create(
            name='test adjust bag', price=0.00, rrp=0.00)

        """ Add product to bag """
        self.client.post(f'/bag/add/{product.product_id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.product_id}/',
            'size': 'false',
        })

        """ adjust quantity of product in bag """
        response = self.client.post(f'/bag/adjust/{product.product_id}/', {
            'quantity': 5,
            'size': 'false',
        })
        self.assertRedirects(response, '/bag/')

    def test_adjust_bag_exception_product_not_in_bag(self):
        """ Create a test product """
        product = Product.objects.create(
            name='test adjust bag', price=0.00, rrp=0.00)

        """ Adjust quantity of product that is not in the bag """
        response = self.client.post(f'/bag/adjust/{product.product_id}/', {
            'quantity': 5,
            'size': 'false',
        })
        self.assertRedirects(response, '/')

    def test_adjust_bag_exception_quantity_not_int(self):
        """ Create a test product """
        product = Product.objects.create(
            name='test adjust bag', price=0.00, rrp=0.00)

        """ Add product to bag """
        self.client.post(f'/bag/add/{product.product_id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.product_id}/',
            'size': 'false',
        })

        """ Adjust quantity of product that is not in the bag """
        response = self.client.post(f'/bag/adjust/{product.product_id}/', {
            'quantity': 'not an integer',
            'size': 'false',
        })
        self.assertRedirects(response, '/bag/')

    def test_remove_from_bag(self):
        """ Create a test product """
        product = Product.objects.create(
            name='test adjust bag', price=0.00, rrp=0.00)

        """ Add product to bag """
        self.client.post(f'/bag/add/{product.product_id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.product_id}/',
            'size': 'test-size',
        })

        """ remove product from bag """
        response = self.client.post(f'/bag/remove/{product.product_id}/', {
            'size': 'test-size',
        })
        self.assertRedirects(response, '/bag/')

    def test_remove_from_bag_size_false(self):
        """ Create a test product """
        product = Product.objects.create(
            name='test adjust bag', price=0.00, rrp=0.00)

        """ Add product to bag """
        self.client.post(f'/bag/add/{product.product_id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.product_id}/',
            'size': 'false',
        })

        """ remove product from bag """
        response = self.client.post(f'/bag/remove/{product.product_id}/', {
            'size': 'false',
        })
        self.assertRedirects(response, '/bag/')

    def test_remove_from_bag_exception_403_redirect(self):
        """ remove product from bag """
        response = self.client.post('/bag/remove/invalid_product_id/')
        self.assertRedirects(response, '/')

    def test_remove_product_not_in_bag(self):
        """ Create a test product """
        product = Product.objects.create(
            name='test adjust bag', price=0.00, rrp=0.00)

        """ remove product from bag """
        response = self.client.post(f'/bag/remove/{product.product_id}/', {
            'size': 'test-size',
        })
        self.assertRedirects(response, '/bag/')
