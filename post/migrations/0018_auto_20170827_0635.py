# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_auto_20170827_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='entries',
            field=models.ManyToManyField(blank=True, to='post.Post'),
        ),
    ]