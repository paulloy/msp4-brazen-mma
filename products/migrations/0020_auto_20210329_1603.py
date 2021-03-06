# Generated by Django 3.1.7 on 2021-03-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20210328_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('bjj', 'BJJ'), ('mma', 'MMA'), ('muay thai', 'MUAY THAI')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('shorts', 'SHORTS'), ('gloves', 'GLOVES'), ('shin guards', 'SHIN GUARDS'), ('mouth guards', 'MOUTH GUARDS'), ('handwraps', 'HANDWRAPS'), ('gi', 'GI'), ('belts', 'BELTS'), ('rash guards', 'RASH GUARDS'), ('spats', 'SPATS')], max_length=20),
        ),
    ]
