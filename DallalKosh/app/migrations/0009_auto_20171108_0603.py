# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 06:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20171108_0549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='good_data',
            new_name='good_date',
        ),
    ]
