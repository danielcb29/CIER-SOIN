# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0007_auto_20150401_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 1, 16, 37, 31, 894953)),
            preserve_default=True,
        ),
    ]
