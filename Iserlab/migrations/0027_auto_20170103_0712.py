# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-03 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0026_remove_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vminstance',
            name='owner',
            field=models.CharField(max_length=20),
        ),
    ]