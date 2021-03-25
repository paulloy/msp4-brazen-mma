from django.urls import path
from . import views

urlpatterns = [
    path('profile_delivery_info/',
         views.profile_delivery_info, name='profile_delivery_info'),
    path('profile_order_history/',
         views.profile_order_history, name='profile_order_history'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
]
