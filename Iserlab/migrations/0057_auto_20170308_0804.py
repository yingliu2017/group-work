# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-08 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0056_auto_20170308_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='start_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='stop_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
