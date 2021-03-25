from django.db import models
import uuid


PRODUCT_CATEGORY_CHOICES = (
    ('select category', 'SELECT CATEGORY'),
    ('bjj', 'BJJ'),
    ('mma', 'MMA'),
    ('muay thai', 'MUAY THAI'),
    ('equipment', 'EQUIPMENT'),
)

PRODUCT_TYPE_CHOICES = (
    ('select type', 'SELECT TYPE'),
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
    ('select gender', 'SELECT GENDER'),
    ('men', 'MEN'),
    ('women', 'WOMEN'),
    ('unisex', 'UNISEX'),
)


class Product(models.Model):
    product_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254, blank=False, null=False)
    description = models.TextField(null=False, blank=False)
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, default="SELECT GENDER")
    sale = models.BooleanField(null=False, blank=False, default=False)
    rrp = models.DecimalField(
        verbose_name='Recommended Retail Price',
        max_digits=6, decimal_places=2, blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(
        max_length=20, choices=PRODUCT_CATEGORY_CHOICES,
        default="SELECT CATEGORY")
    product_type = models.CharField(
        max_length=20, choices=PRODUCT_TYPE_CHOICES, default="SELECT TYPE")
    image = models.ImageField(upload_to='product_images/',
                              blank=False, null=False,
                              default='products/static/ \
                                  product_img/placeholder.jpg')

    def __str__(self):
        return self.name


class ProductSizesStock(models.Model):
    product_sizes_quantity_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(
        'Product', on_delete=models.CASCADE, null=True)
    size = models.CharField(max_length=254, null=True)
    stock = models.PositiveIntegerField()

    def __str__(self):
        my_tuple = (str(self.product_id), str(self.size))
        return ' | '.join(my_tuple)

    class Meta:
        verbose_name_plural = 'Product Sizes and Stock'
