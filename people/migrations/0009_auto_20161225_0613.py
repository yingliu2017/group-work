# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-25 06:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20161225_0527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-pub_date']},
        ),
    ]
