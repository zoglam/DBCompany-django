# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-18 08:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_payment1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment1',
            name='nds',
        ),
        migrations.RemoveField(
            model_name='payment1',
            name='price_nds',
        ),
    ]
