# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-20 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20181220_0220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='dateOfBirth',
            new_name='DateOfBirth',
        ),
        migrations.AddField(
            model_name='customer',
            name='degree_certificate',
            field=models.FileField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
