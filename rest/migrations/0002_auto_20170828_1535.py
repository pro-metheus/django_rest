# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiauth',
            name='api_key',
            field=models.CharField(default=uuid.UUID('8464e836-162f-4d25-b18c-aee477ba8243'), max_length=36),
        ),
    ]
