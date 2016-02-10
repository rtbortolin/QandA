# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 16:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_in', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
                ('is_accepted', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnswerVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_in', models.DateTimeField(default=django.utils.timezone.now)),
                ('grade', models.CharField(choices=[(b'P', b'Positive'), (b'N', b'Negative')], max_length=1)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Answer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_in', models.DateTimeField(default=django.utils.timezone.now)),
                ('grade', models.CharField(choices=[(b'P', b'Positive'), (b'N', b'Negative')], max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserExtension',
            fields=[
                ('created_in', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_in', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('points', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updater',
        ),
        migrations.RemoveField(
            model_name='usercustom',
            name='user',
        ),
        migrations.AlterField(
            model_name='question',
            name='created_in',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_in',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='UserCustom',
        ),
        migrations.AddField(
            model_name='questionvote',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question'),
        ),
        migrations.AddField(
            model_name='questionvote',
            name='voter',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.UserExtension'),
        ),
        migrations.AddField(
            model_name='answervote',
            name='voter',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.UserExtension'),
        ),
        migrations.AddField(
            model_name='answer',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_creator_id', to='app.UserExtension'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='updater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_updater_id', to='app.UserExtension'),
        ),
        migrations.AddField(
            model_name='question',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='q_creator_id', to='app.UserExtension'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='updater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='q_updater_id', to='app.UserExtension'),
            preserve_default=False,
        ),
    ]