# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-07 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0006_auto_20190507_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fees',
            field=models.IntegerField(default=1),
        ),
    ]