# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-25 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='semail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='smobile',
            field=models.IntegerField(),
        ),
    ]