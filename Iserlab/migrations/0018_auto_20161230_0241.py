# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-30 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0017_auto_20161227_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='vmimage',
            name='flavor',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='vmimage',
            name='keypair',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
