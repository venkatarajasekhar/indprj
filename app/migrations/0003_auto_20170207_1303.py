# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-07 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170205_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='session_id',
        ),
        migrations.AlterField(
            model_name='session',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
