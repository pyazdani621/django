# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lastName',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
    ]