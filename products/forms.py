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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'input-width'
            self.fields[field].required = False
