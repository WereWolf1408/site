# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=2000, blank=True)),
                ('image_source', models.CharField(max_length=200, blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('bookmark', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'publication',
                'ordering': ['-date'],
            },
        ),
    ]
