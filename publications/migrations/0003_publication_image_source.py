# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_publication_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='image_source',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
