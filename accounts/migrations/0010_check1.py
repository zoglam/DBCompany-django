# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-17 19:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20181213_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('date', models.DateField()),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Client')),
            ],
        ),
    ]
