# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-27 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0013_auto_20161227_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='cidr',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='network',
            name='ip_version',
            field=models.CharField(max_length=2, null=True),
        ),
    ]