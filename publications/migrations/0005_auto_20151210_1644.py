# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_publication_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelTable(
            name='publication',
            table='publication',
        ),
    ]
