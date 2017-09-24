# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('attended', models.BooleanField()),
                ('remarks', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('sex', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('picture', models.ImageField(upload_to='static/images')),
                ('enrolment_date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Responsible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('sex', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('picture', models.ImageField(upload_to='static/images')),
                ('profession', models.CharField(max_length=255)),
                ('education_level', models.CharField(max_length=70)),
                ('reslationshipWithPupil', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScoreRecorded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_first_control', models.DecimalField(decimal_places=2, max_digits=6)),
                ('score_second_control', models.DecimalField(decimal_places=2, max_digits=6)),
                ('score_third_control', models.DecimalField(decimal_places=2, max_digits=6)),
                ('score_fourth_control', models.DecimalField(decimal_places=2, max_digits=6)),
                ('score_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Course')),
                ('pupil_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Pupil')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('sex', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('picture', models.ImageField(upload_to='static/images')),
                ('academic_level', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pupil',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Responsible'),
        ),
        migrations.AddField(
            model_name='course',
            name='grade_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Grade'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='grade_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Grade'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='pupil_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Pupil'),
        ),
    ]