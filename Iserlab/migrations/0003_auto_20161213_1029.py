# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-13 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0002_auto_20161213_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_username', models.CharField(max_length=50)),
                ('stu_password', models.CharField(max_length=50)),
                ('stu_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Experiment',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]