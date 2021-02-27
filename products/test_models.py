from django.test import TestCase
from .models import (Product, ProductCategory,
                     ProductType, ProductGender, ProductSizesStock)
import random


class TestModels(TestCase):

    def test_productcategory_string_method_returns_name(self):
        item = ProductCategory.objects.create(name='Test String Method')
        self.assertEqual(str(item), 'Test String Method')

    def test_producttype_string_method_returns_name(self):
        item = ProductType.objects.create(name='Test String Method')
        self.assertEqual(str(item), 'Test String Method')

    def test_productgender_string_method_returns_name(self):
        item = ProductGender.objects.create(name='Test String Method')
        self.assertEqual(str(item), 'Test String Method')

    def test_product_string_method_returns_name(self):
        item = Product.objects.create(
            name='Test String Method', rrp='0.00', price='0.00')
        self.assertEqual(str(item), 'Test String Method')

    def test_productsizesstock_string_method_returns_tuple(self):
        item = ProductSizesStock.objects.create(
            size='Test String Method', stock=random.randint(0, 100))
        self.assertEqual(str(item), f'{item.product_id} | {item.size}')
