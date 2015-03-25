# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0001_initial'),
        ('teacher', '0001_initial'),
        ('calificacionesCertificados', '0002_certificado_cohorte'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificado',
            name='leader_teacher',
            field=models.OneToOneField(to='teacher.LeaderTeacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificacion',
            name='actividad',
            field=models.OneToOneField(to='cursosCohortesActividades.Actividad'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificacion',
            name='leader_teacher',
            field=models.OneToOneField(to='teacher.LeaderTeacher'),
            preserve_default=True,
        ),
    ]
