# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0021_auto_20170924_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='channel',
            field=models.CharField(default='Web', max_length=50),
        ),
    ]
