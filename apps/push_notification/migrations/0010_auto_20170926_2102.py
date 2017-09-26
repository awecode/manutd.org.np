# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('push_notification', '0009_auto_20170911_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdevice',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdevice',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
