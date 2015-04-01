# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historiaAcademicaLaboral', '0004_auto_20150329_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiaacademica',
            name='activo',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='historialaboral',
            name='activo',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
