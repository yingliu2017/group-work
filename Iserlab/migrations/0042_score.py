# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-06 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0041_auto_20170306_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('times', models.IntegerField(default=0)),
                ('situation', models.CharField(default='Undo', max_length=10)),
                ('finishedTime', models.DateTimeField(blank=True, null=True)),
                ('result', models.CharField(blank=True, max_length=500, null=True)),
                ('result_exp_id', models.CharField(blank=True, max_length=10, null=True)),
                ('reportUrl', models.URLField(blank=True, null=True)),
                ('exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Iserlab.Experiment')),
                ('scorer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Iserlab.User')),
                ('stu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Iserlab.Student')),
            ],
        ),
    ]
