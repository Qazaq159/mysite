# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2023-09-12 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20230822_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='create_date',
            field=models.DateTimeField(default='2000-12-31 00:00'),
        ),
    ]
