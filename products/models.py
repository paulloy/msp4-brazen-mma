from django.db import models
import uuid


PRODUCT_CATEGORY_CHOICES = (
    ('bjj', 'BJJ'),
    ('mma', 'MMA'),
    ('muay thai', 'MUAY THAI'),
    ('equipment', 'EQUIPMENT'),
)

PRODUCT_TYPE_CHOICES = (
    ('shorts', 'SHORTS'),
    ('gloves', 'GLOVES'),
    ('shin guards', 'SHIN GUARDS'),
    ('mouth guards', 'MOUTH GUARDS'),
    ('handwraps', 'HANDWRAPS'),
    ('gi', 'GI'),
    ('belts', 'BELTS'),
    ('rash guards', 'RASH GUARDS'),
    ('spats', 'SPATS'),
    ('groin guards', 'GROIN GUARDS'),
    ('kick shields', 'KICK SHIELDS'),
    ('belly pads', 'BELLY PADS'),
    ('punch bags', 'PUNCH BAGS'),
    ('grappling dummies', 'GRAPPLING DUMMIES'),
    ('joint support', 'JOINT SUPPORT'),
)

GENDER_CHOICES = (
    ('men', 'MEN'),
    ('women', 'WOMEN'),
    ('unisex', 'UNISEX'),
)

ALLOWED_SIZES = (
    ('xs', 'XS'),
    ('s', 'S'),
    ('m', 'M'),
    ('l', 'L'),
    ('xl', 'XL'),
    ('false', 'FALSE'),
)


class Product(models.Model):
    product_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254, blank=False, null=False)
    description = models.TextField(null=False, blank=False)
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, blank=False, null=False)
    sale = models.BooleanField(null=False, blank=False, default=False)
    rrp = models.DecimalField(
        verbose_name='Recommended Retail Price',
        max_digits=6, decimal_places=2, blank=False, null=False)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=False, null=False)
    category = models.CharField(
        max_length=20, choices=PRODUCT_CATEGORY_CHOICES,
        blank=False, null=False)
    product_type = models.CharField(
        max_length=20, choices=PRODUCT_TYPE_CHOICES, blank=False, null=False)
    image = models.ImageField(upload_to='product_images/',
                              blank=False, null=False,
                              default='products/static/ \
                                  product_img/placeholder.jpg')

    def __str__(self):
        return self.name


class ProductSizesStock(models.Model):
    product_sizes_stock_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(
        'Product', on_delete=models.CASCADE, null=True)
    size = models.CharField(
        max_length=10, choices=ALLOWED_SIZES, null=True)
    stock = models.PositiveIntegerField()

    def __str__(self):
        my_tuple = (str(self.product_id), str(self.size))
        return ' | '.join(my_tuple)

    class Meta:
        verbose_name_plural = 'Product Sizes and Stock'
