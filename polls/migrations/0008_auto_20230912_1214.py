# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2023-09-12 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20230912_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='create_date',
            field=models.DateTimeField(blank=True, default='2000-01-01', null=True),
        ),
    ]
