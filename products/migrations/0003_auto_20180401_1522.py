# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-01 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_productlist_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.FloatField(),
        ),
    ]
