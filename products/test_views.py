from django.test import TestCase, RequestFactory, Client
from django.shortcuts import HttpResponse
from django.urls import reverse
from . import models
from . import views
import random


class TestViews(TestCase):

    def setUp(self):
        # Some tests need access to the request factory.
        self.factory = RequestFactory()

    # all_products()

    def test_all_products_view(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_category_and_product_type_in_get_request(self):
        c = Client()
        category = random.sample(models.PRODUCT_CATEGORY_CHOICES, k=1)[0][0]
        product_type = random.sample(models.PRODUCT_TYPE_CHOICES, k=1)[0][0]
        response = c.get(
            f'/products/?category={category}&product_type={product_type}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_category_in_get_request(self):
        c = Client()
        category = random.sample(models.PRODUCT_CATEGORY_CHOICES, k=1)[0][0]
        response = c.get(f'/products/?category={category}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_q_in_get_request(self):
        c = Client()
        response = c.get('/products/?q=user_custom_value')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sort_and_direction_in_get_request(self):
        c = Client()
        sort = ['price', 'name']
        direction = ['asc', 'desc']
        for sortkey in sort:
            for directionkey in direction:
                response = c.get(
                    f'/products/?sort={sortkey}&direction={directionkey}')
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'products/products.html')

    def test_filters_in_get_request(self):
        c = Client()
        filters = ['MEN', 'WOMEN', 'UNISEX']
        for filter_key in filters:
            response = c.get(f'/products/?filters={filter_key}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'products/products.html')

    # product_details()

    def test_product_details_view(self):
        product = models.Product.objects.create(
            name='Test Product', price='0.00', rrp='1.00')
        sizes_no_stock = models.ProductSizesStock.objects.create(
            product_id=product, size='Test Size Stock 0', stock=0)
        sizes_less_than_five = models.ProductSizesStock.objects.create(
            product_id=product, size='Test Size Stock < 5', stock=3)
        response = self.client.get(f'/products/{product.product_id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')
