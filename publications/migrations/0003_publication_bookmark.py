# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_remove_publication_bookmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='bookmark',
            field=models.BooleanField(default=False),
        ),
    ]
