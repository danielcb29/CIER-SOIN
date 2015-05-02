# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0015_curso_semanas'),
        ('calificacionesCertificados', '0008_remove_calificacion_actividad'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion',
            name='actividad_cohorte',
            field=models.ForeignKey(default=0, to='cursosCohortesActividades.Actividad_Cohorte'),
            preserve_default=False,
        ),
    ]
