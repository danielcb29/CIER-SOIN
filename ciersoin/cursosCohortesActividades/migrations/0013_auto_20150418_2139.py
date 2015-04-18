# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0012_auto_20150418_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='fecha_entrega',
        ),
        migrations.RemoveField(
            model_name='cohorte',
            name='actividad',
        ),
        migrations.AddField(
            model_name='curso',
            name='semanas',
            field=models.IntegerField(default=7, choices=[(6, 6), (7, 7)]),
            preserve_default=True,
        ),
    ]
