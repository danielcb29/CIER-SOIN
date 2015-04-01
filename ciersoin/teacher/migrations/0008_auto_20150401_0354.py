# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_auto_20150329_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='cedula',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
    ]
