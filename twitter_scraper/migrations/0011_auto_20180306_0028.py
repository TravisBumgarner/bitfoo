# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_scraper', '0010_auto_20180306_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.TextField(blank=True, null=True),
        ),
    ]