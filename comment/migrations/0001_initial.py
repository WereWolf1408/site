# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_publication_bookmark'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('text', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('enot', models.CharField(max_length=100)),
                ('publication', models.ForeignKey(null=True, to='publications.Publication')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'ordering': ['-date'],
                'db_table': 'comment',
            },
        ),
    ]
