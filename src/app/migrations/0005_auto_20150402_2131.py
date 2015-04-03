# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150402_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='name',
        ),
        migrations.AlterField(
            model_name='option',
            name='option',
            field=models.IntegerField(default=4),
            preserve_default=True,
        ),
    ]
