# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calificacionesCertificados', '0006_calificacion_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificacion',
            name='actividad',
            field=models.ForeignKey(to='cursosCohortesActividades.Actividad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='leader_teacher',
            field=models.ForeignKey(to='teacher.LeaderTeacher'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='certificado',
            name='leader_teacher',
            field=models.ForeignKey(to='teacher.LeaderTeacher'),
            preserve_default=True,
        ),
    ]
