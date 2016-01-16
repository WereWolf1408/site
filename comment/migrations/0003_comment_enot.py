# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_remove_comment_enot'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='enot',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
