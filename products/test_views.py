from django.test import TestCase, RequestFactory, Client
from .models import (Product, ProductCategory,
                     ProductType, ProductGender, ProductSizesStock)
from .views import product_details, all_products


class TestViews(TestCase):

    def setUp(self):
        # Some tests need access to the request factory.
        self.factory = RequestFactory()

    def test_get_products_view(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_details_view(self):
        item = Product.objects.create(
            name='Test product details view', rrp='0.00', price='0.00')
        response = self.client.get(f'/products/{item.product_id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')

    def test_category_and_product_type_in_get_request(self):
        category = ProductCategory.objects.create(name='Test Category')
        product_type = ProductType.objects.create(name='Test Product Type')
        item = Product.objects.create(
            name='Test Category and Product_Type in GET Request',
            category=category, product_type=product_type,
            rrp='0.00', price='0.00')
        response = self.client.get(
            f'/products/?category={item.category}&\
                product_type={item.product_type}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_q_in_get_request(self):
        q = 'test q in GET request'
        response = self.client.get(f'/products/?q={q}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_save_subtraction(self):
        item = Product.objects.create(
            name='Test Save Subtraction',
            rrp='25.00', price='15.00')
        request = self.factory.get(f'/products/{item.product_id}')
        response = product_details(request, item.product_id)
        self.assertEqual(response.status_code, 200)

    def test_all_products(self):
        category = ProductCategory.objects.create(name='Test Category')
        product_type = ProductType.objects.create(name='Test Product Type')
        item = Product.objects.create(
            name='Test Category and Product_Type in GET Request',
            category=category, product_type=product_type,
            rrp='0.00', price='0.00')
        c = Client()
        response = c.get('/products/', {
            'category': item.category, 'product_type': item.product_type})
        self.assertEqual(response.status_code, 200)

    def test_q_not_in_get_request(self):
        c = Client()
        response = c.get('/products/', {'q': ''})
        self.assertRedirects(response, '/products/', status_code=302,
                             target_status_code=200,
                             fetch_redirect_response=True)

