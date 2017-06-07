# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-07 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InviteBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_found', models.IntegerField(default=0)),
                ('new_added', models.IntegerField(default=0)),
                ('payload', models.TextField()),
            ],
        ),
    ]
