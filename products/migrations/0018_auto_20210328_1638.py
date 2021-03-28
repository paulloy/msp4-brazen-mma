# Generated by Django 3.1.7 on 2021-03-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20210328_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('bjj', 'BJJ'), ('mma', 'MMA'), ('muay thai', 'MUAY THAI'), ('equipment', 'EQUIPMENT')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('men', 'MEN'), ('women', 'WOMEN'), ('unisex', 'UNISEX')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('shorts', 'SHORTS'), ('gloves', 'GLOVES'), ('shin guards', 'SHIN GUARDS'), ('mouth guards', 'MOUTH GUARDS'), ('handwraps', 'HANDWRAPS'), ('gi', 'GI'), ('belts', 'BELTS'), ('rash guards', 'RASH GUARDS'), ('spats', 'SPATS'), ('groin guards', 'GROIN GUARDS'), ('kick shields', 'KICK SHIELDS'), ('belly pads', 'BELLY PADS'), ('punch bags', 'PUNCH BAGS'), ('grappling dummies', 'GRAPPLING DUMMIES'), ('joint support', 'JOINT SUPPORT')], max_length=20),
        ),
    ]