# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-09 10:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0060_delivery_update_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagecart',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='networkcart',
            old_name='user_id',
            new_name='user',
        ),
    ]
