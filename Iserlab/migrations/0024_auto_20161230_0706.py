# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-30 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0023_auto_20161230_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='tenant_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='network',
            name='ip_version',
            field=models.CharField(default='4', max_length=2, null=True),
        ),
    ]
