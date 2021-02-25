from django.db import models
import uuid


class ProductCategory(models.Model):
    product_category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product Categories'


class ProductType(models.Model):
    product_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product Types'


class ProductGender(models.Model):
    product_gender_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product Genders'


class Product(models.Model):
    product_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254, blank=False, null=False)
    description = models.TextField(null=False, blank=False)
    gender = models.ForeignKey(
        'ProductGender', on_delete=models.CASCADE, null=True, blank=False)
    sale = models.BooleanField(null=False, blank=False, default=False)
    rrp = models.DecimalField(
        verbose_name='Recommended Retail Price',
        max_digits=6, decimal_places=2, blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        'ProductCategory', on_delete=models.CASCADE,
        blank=False, null=True)
    product_type = models.ForeignKey(
        'ProductType', on_delete=models.CASCADE,
        blank=False, null=True)
    image = models.ImageField(upload_to='product_img/',
                              blank=False, null=False,
                              default='products/static/\
                                  product_img/placeholder.jpg')

    def __str__(self):
        return self.name


class ProductSizesStock(models.Model):
    product_sizes_quantity_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(
        'Product', on_delete=models.CASCADE, null=True)
    size = models.CharField(max_length=254)
    stock = models.PositiveIntegerField()

    def __str__(self):
        my_tuple = (str(self.product_id), str(self.size))
        return ' | '.join(my_tuple)

    class Meta:
        verbose_name_plural = 'Product Sizes & Quantities'
