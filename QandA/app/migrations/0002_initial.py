# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 16:05
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(default=datetime.datetime(2016, 2, 10, 16, 5, 8, 79000, tzinfo=utc))),
                ('updated_in', models.DateTimeField(default=datetime.datetime(2016, 2, 10, 16, 5, 8, 79000, tzinfo=utc))),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserCustom',
            fields=[
                ('created_in', models.DateTimeField(default=datetime.datetime(2016, 2, 10, 16, 5, 8, 79000, tzinfo=utc))),
                ('updated_in', models.DateTimeField(default=datetime.datetime(2016, 2, 10, 16, 5, 8, 79000, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('points', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='question',
            old_name='titile',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='question',
            name='created_in',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 10, 16, 5, 8, 79000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_in',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 10, 16, 5, 8, 79000, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_id', to='app.UserCustom'),
        ),
        migrations.AddField(
            model_name='post',
            name='updater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updater_id', to='app.UserCustom'),
        ),
    ]
