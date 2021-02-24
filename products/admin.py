from django.contrib import admin
from .models import (Product, ProductCategory,
                     ProductType, ProductGender, ProductSizesStock)


class ProductSizesStockAdminInline(admin.TabularInline):
    model = ProductSizesStock
    readonly_fields = ('product_id',)


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductSizesStockAdminInline,)

    list_display = ('product_id', 'name', 'price', 'sale')

    readonly_fields = ('product_id',)

    ordering = ('product_id',)


admin.site.register(ProductCategory)
admin.site.register(ProductType)
admin.site.register(ProductGender)
admin.site.register(Product, ProductAdmin)
