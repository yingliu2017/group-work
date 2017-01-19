# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-03 07:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0024_auto_20161230_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(blank=True, max_length=100, null=True)),
                ('stuCount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ManyToManyField(to='Iserlab.Student')),
            ],
        ),
        migrations.RemoveField(
            model_name='expinstance',
            name='creator',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='student', max_length=50),
        ),
        migrations.AddField(
            model_name='vminstance',
            name='exp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Iserlab.ExpInstance'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='delivery',
            name='stu_username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Iserlab.Group'),
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Iserlab.User'),
        ),
    ]
