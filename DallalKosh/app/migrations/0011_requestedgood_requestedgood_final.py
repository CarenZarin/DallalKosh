# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_good_good_is_final'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestedgood',
            name='requestedgood_final',
            field=models.BooleanField(default=False),
        ),
    ]