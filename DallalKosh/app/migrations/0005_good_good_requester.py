# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 05:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20171107_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='good_requester',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='good_requester', to='app.RequestedGood'),
        ),
    ]
