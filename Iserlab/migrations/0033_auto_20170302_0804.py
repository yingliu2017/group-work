# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-02 08:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0032_auto_20170302_0803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='exp_id',
            new_name='exp',
        ),
    ]
