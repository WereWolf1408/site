# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publications', '0005_auto_20151210_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('publication', models.ForeignKey(null=True, to='publications.Publication')),
                ('user', models.ForeignKey(related_name='User', default='Anton', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
                'db_table': 'comment',
            },
        ),
    ]
