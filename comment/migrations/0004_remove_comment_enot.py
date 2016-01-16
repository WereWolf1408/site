# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_comment_enot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='enot',
        ),
    ]
