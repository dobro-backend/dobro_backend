# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobro', '0002_auto_20170910_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=256),
        ),
    ]