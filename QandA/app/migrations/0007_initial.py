# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='updater',
        ),
        migrations.RemoveField(
            model_name='answervote',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='answervote',
            name='voter',
        ),
        migrations.RemoveField(
            model_name='question',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='question',
            name='updater',
        ),
        migrations.RemoveField(
            model_name='questionvote',
            name='question',
        ),
        migrations.RemoveField(
            model_name='questionvote',
            name='voter',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.RemoveField(
            model_name='userextension',
            name='user',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='AnswerVote',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='QuestionVote',
        ),
        migrations.DeleteModel(
            name='UserExtension',
        ),
    ]
