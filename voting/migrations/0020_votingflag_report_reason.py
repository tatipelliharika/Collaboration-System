# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0019_votingflag_reportflag'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingflag',
            name='report_reason',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]