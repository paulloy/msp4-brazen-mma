# Generated by Django 3.1.7 on 2021-03-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20210308_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products/static/                                   product_img/placeholder.jpg', upload_to='product_images/'),
        ),
    ]