# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20171108_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestedgood',
            name='requestgood_data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
