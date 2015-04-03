# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0008_auto_20150401_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='fecha_entrega',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
