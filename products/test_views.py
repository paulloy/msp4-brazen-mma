from django.test import TestCase

from . import models
from .models import Product, ProductSizesStock

import random


class TestViews(TestCase):

    """ all_products() """
    def test_all_products_view(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_category_and_product_type_in_get_request(self):
        category = random.sample(models.PRODUCT_CATEGORY_CHOICES, k=1)[0][0]
        product_type = random.sample(models.PRODUCT_TYPE_CHOICES, k=1)[0][0]
        response = self.client.post(
            f'/products/?category={category}&product_type={product_type}')
        self.assertEqual(response.status_code, 200)

    def test_category_in_get_request(self):
        category = random.sample(models.PRODUCT_CATEGORY_CHOICES, k=1)[0][0]
        response = self.client.post(
            f'/products/?category={category}')
        self.assertEqual(response.status_code, 200)

    def test_q_in_get_request(self):
        response = self.client.post(
            '/products/?q=searched_value')
        self.assertEqual(response.status_code, 200)

    def test_sort_and_direction_in_get_request(self):
        sort = ['price', 'name']
        direction = ['asc', 'desc']
        for sortkey in sort:
            for directionkey in direction:
                response = self.client.post(
                    f'/products/?sort={sortkey}&direction={directionkey}')
                self.assertEqual(response.status_code, 200)

    def test_filters_in_get_request(self):
        filters = ['MEN', 'WOMEN', 'UNISEX', 'DISCOUNTED']
        for filter_key in filters:
            response = self.client.post(
                f'/products/?filters={filter_key}')
            self.assertEqual(response.status_code, 200)

    """ product_details() """

    def test_product_details_view(self):
        """ create product """
        product = Product.objects.create(
            name='Test Product', price='5.00', rrp='10.00')

        """ add sizes to product """
        """ stock <=5  """
        ProductSizesStock.objects.create(
            product_id=product, size="test_size", stock=3)
        """ stock = 0 """
        ProductSizesStock.objects.create(
            product_id=product, size="test_size_2", stock=0)

        response = self.client.get(f'/products/{product.product_id}/')
        self.assertEqual(response.status_code, 200)

    def test_product_size_false(self):
        """ create product """
        product = Product.objects.create(
            name='Test Product', price='5.00', rrp='10.00')

        """ add sizes to product """
        """ size false  """
        ProductSizesStock.objects.create(
            product_id=product, size="false", stock=3)

        response = self.client.get(f'/products/{product.product_id}/')
        self.assertEqual(response.status_code, 200)

    """ ajax_q_request() """
    def test_ajax_q_request(self):
        response = self.client.post('/products/ajax_q/?q=bjj')
        print(response)
        self.assertEqual(response.status_code, 200)
