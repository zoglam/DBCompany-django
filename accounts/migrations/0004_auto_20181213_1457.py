# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-13 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181213_1453'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
    ]
