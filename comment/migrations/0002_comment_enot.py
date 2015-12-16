# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='enot',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
