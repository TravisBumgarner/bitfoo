# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 00:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_scraper', '0011_auto_20180306_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='favorited',
        ),
    ]