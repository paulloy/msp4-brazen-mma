# Generated by Django 3.1.7 on 2021-03-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210224_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('bjj', 'BJJ'), ('mma', 'MMA'), ('muay thai', 'MUAY THAI'), ('equipment', 'EQUIPMENT')], default='SELECT CATEGORY', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('men', 'MEN'), ('women', 'WOMEN'), ('unisex', 'UNISEX')], default='SELECT GENDER', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products/static/                                   product_img/placeholder.jpg', upload_to='product_img/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('shorts', 'SHORTS'), ('gloves', 'GLOVES'), ('shin guards', 'SHIN GUARDS'), ('mouth guards', 'MOUTH GUARDS'), ('handwraps', 'HANDWRAPS'), ('gi', 'GI'), ('belts', 'BELTS'), ('rash guards', 'RASH GUARDS'), ('spats', 'SPATS'), ('groin guards', 'GROIN GUARDS'), ('kick shields', 'KICK GUARDS'), ('belly pads', 'BELLY PADS'), ('punch bags', 'PUNCH BAGS'), ('grappling dummies', 'GRAPPLING DUMMIES')], default='SELECT TYPE', max_length=20),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='ProductGender',
        ),
        migrations.DeleteModel(
            name='ProductType',
        ),
    ]
