# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0002_poll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection', models.IntegerField()),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='poll_app.Poll')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voters', to='poll_app.User')),
            ],
            managers=[
                ('voteManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
