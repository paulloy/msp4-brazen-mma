from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<uuid:product_id>/', views.product_details, name='product_details'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<uuid:product_id>', views.edit_product, name='edit_product'),
    path('delete/<uuid:product_id>',
         views.delete_product, name='delete_product'),
]
