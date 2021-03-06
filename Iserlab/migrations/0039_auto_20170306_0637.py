# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-06 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0038_score_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='finishedTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='reportUrl',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='result',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='result_exp_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='situation',
            field=models.CharField(default='Undo', max_length=10),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='exp_result',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
