# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 01:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0016_remove_attendance_grade_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='pupil_id',
            new_name='pupil',
        ),
    ]
