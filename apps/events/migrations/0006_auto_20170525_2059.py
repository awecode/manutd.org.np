# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 15:14
from __future__ import unicode_literals

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=froala_editor.fields.FroalaField(blank=True, null=True),
        ),
    ]
