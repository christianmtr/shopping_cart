# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
