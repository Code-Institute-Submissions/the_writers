# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 06:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20170826_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition',
            old_name='name',
            new_name='title',
        ),
    ]
