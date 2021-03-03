from django.contrib import admin
from .models import Product, ProductSizesStock


class ProductSizesStockAdminInline(admin.TabularInline):
    model = ProductSizesStock
    readonly_fields = ('product_id',)


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductSizesStockAdminInline,)

    list_display = (
        'product_id', 'name', 'category',
        'product_type', 'gender', 'price', 'sale')

    readonly_fields = ('product_id',)

    ordering = ('product_id',)


admin.site.register(Product, ProductAdmin)
