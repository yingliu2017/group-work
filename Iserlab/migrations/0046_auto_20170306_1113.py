# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-06 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0045_auto_20170306_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
