# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-29 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nip', '0005_auto_20180329_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.BinaryField(blank=True),
        ),
    ]
