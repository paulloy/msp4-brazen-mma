from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ajax/', views.ajax_request, name='ajax_request')
]
