# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-29 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nip', '0006_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
