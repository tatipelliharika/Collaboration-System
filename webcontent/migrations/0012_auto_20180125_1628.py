# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-25 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcontent', '0011_faq_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='order',
            field=models.FloatField(default=0.0),
        ),
    ]