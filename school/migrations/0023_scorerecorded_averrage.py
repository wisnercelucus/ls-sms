# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-15 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0022_auto_20171008_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorerecorded',
            name='averrage',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]