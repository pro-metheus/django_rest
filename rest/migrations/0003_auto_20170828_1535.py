# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20170828_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiauth',
            name='api_key',
            field=models.CharField(default=uuid.UUID('dac483ba-d424-4f3b-900c-3610f835efec'), max_length=36),
        ),
    ]