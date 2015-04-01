# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calificacionesCertificados', '0005_remove_calificacion_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion',
            name='valor',
            field=models.FloatField(default=-1),
            preserve_default=True,
        ),
    ]
