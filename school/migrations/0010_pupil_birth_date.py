# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 23:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20170821_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupil',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
