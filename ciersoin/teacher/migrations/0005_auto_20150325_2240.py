# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20150325_2235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaderteacher',
            options={'permissions': (('ver_calificaciones', 'Puede ver calif descargar cert'), ('editar_datos_personales', 'Puede editar sus propios datos'), ('listar_LT', 'Se permite editar, activar , desactivar'), ('matricular_lt', 'Matricular estudiantes a cohortes'))},
        ),
        migrations.AlterModelOptions(
            name='masterteacher',
            options={'permissions': (('anadir_calificaciones', 'Puede calificar cursos'), ('editar_datos_personales', 'Puede editar sus propios datos'))},
        ),
    ]
