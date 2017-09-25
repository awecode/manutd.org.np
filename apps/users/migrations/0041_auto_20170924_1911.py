# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0040_auto_20170924_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardstatus',
            name='status',
            field=models.CharField(choices=[('Awaiting Print', 'Awaiting Print'), ('Printed', 'Printed'), ('Delivered', 'Delivered')], default='Awaiting Print', max_length=20),
        ),
    ]