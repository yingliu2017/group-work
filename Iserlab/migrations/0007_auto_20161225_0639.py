# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-25 06:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0006_auto_20161225_0613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'ordering': ['-delivery_time']},
        ),
        migrations.AlterModelOptions(
            name='experiment',
            options={'ordering': ['-exp_createtime']},
        ),
        migrations.AlterModelOptions(
            name='expimage',
            options={'ordering': ['-createtime']},
        ),
        migrations.AlterModelOptions(
            name='expinstance',
            options={'ordering': ['-createtime']},
        ),
        migrations.AlterModelOptions(
            name='expnetwork',
            options={'ordering': ['-createtime']},
        ),
        migrations.AlterModelOptions(
            name='network',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='vminstance',
            options={'ordering': ['-createtime']},
        ),
    ]