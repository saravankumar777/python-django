# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-18 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Mobile_number',
            field=models.IntegerField(),
        ),
    ]
