# Generated by Django 2.1.1 on 2019-05-20 03:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_task', models.IntegerField(default=0)),
                ('daily_task_done', models.BooleanField(default=False)),
                ('daily_task_done_time', models.DateTimeField(default=datetime.datetime(2019, 5, 18, 5, 16, 43, 526258))),
                ('current_step', models.IntegerField(default=0)),
                ('timezone', models.CharField(blank=True, default='0', max_length=255, null=True)),
                ('completed_at', models.TextField(blank=True, default='', null=True)),
                ('my_tasks_completed', models.IntegerField(default=0)),
                ('number_of_tasks', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
