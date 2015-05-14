# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0011_auto_20150409_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='cedula',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
