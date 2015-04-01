# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0004_aspirante'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='activo',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cohorte',
            name='activo',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='curso',
            name='activo',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
