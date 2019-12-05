# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-20 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20181220_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'Female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='martialStatus',
            field=models.CharField(choices=[('1', 'Single'), ('2', 'Married'), ('3', 'divorced')], default='1', max_length=25),
        ),
        migrations.AlterField(
            model_name='customer',
            name='partner_Martial_status',
            field=models.CharField(default=0, max_length=25),
        ),
    ]
