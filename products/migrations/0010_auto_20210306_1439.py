# Generated by Django 3.1.7 on 2021-03-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210306_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products/static/                                   product_img/placeholder.jpg', upload_to='static/'),
        ),
    ]
