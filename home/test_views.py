from django.test import TestCase, RequestFactory, Client
from products.models import Product, PRODUCT_CATEGORY_CHOICES,\
     PRODUCT_TYPE_CHOICES
import random
from django.core import serializers


class TestViews(TestCase):

    # index()
    def test_get_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
    
    # ajax_request()
    # def test_ajax_request(self):
    #     all_products = Product.objects.all()
    #     category = random.sample(PRODUCT_CATEGORY_CHOICES, k=1)[0][0]
    #     product_type = random.sample(PRODUCT_TYPE_CHOICES, k=1)[0][0]
    #     c = Client()
    #     response = c.get(f'/?category={category}&product_type={product_type}')
    #     product_preview = serializers.serialize("json", response.content) 
        
    #     self.assertEqual(response.status_code, 200)
    #     self.assertJSONEqual(
    #         str(product_preview, encoding='utf8'),
    #         {'status': 'success'}
    #     )

    def test_category_and_product_type_in_get_request(self):
        c = Client()
        category = PRODUCT_CATEGORY_CHOICES
        product_type = PRODUCT_TYPE_CHOICES
        for i in category:
            for j in product_type:
                response = c.get(
                    f'/?category={i}&product_type={j}')
                
                print(product_preview)
                self.assertEqual(response.status_code, 200)
                # self.assertJSONEqual(
                #     str(product_preview.json(), encoding='utf8'),
                #     {'status': 'success'}
                # )
