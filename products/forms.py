from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, ProductSizesStock


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)


class ProductSizesStockForm(forms.ModelForm):

    class Meta:
        model = ProductSizesStock
        exclude = ('product_id',)
