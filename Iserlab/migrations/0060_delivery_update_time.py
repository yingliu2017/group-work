# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-08 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0059_auto_20170308_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
