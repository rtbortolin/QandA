# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 15:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(default=datetime.datetime(2016, 2, 10, 15, 18, 19, 40000, tzinfo=utc))),
                ('updated_in', models.DateTimeField(default=datetime.datetime(2016, 2, 10, 15, 18, 19, 40000, tzinfo=utc))),
                ('body', models.TextField()),
                ('titile', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]