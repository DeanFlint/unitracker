# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='status',
            field=models.CharField(choices=[('todo', 'To Do'), ('inprogress', 'In Progress'), ('done', 'Done')], default='todo', max_length=12),
        ),
    ]
