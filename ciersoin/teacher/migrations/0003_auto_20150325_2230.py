# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20150325_2217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaderteacher',
            options={'permissions': (('anadir_calificaciones', 'Puede calificar cursos'), ('editar_datos_personales', 'Puede editar sus propios datos'), ('listar_LT', 'Se permite listar lts para editar informacion y activar , desactivar'), ('matricular_lt', 'Matricular (Asignar) los estudiantes a las cohortes'))},
        ),
        migrations.AlterModelOptions(
            name='masterteacher',
            options={'permissions': (('ver_calificaciones', 'Puede ver sus calificaciones y descargar certificados'), ('editar_datos_personales', 'Puede editar sus propios datos'))},
        ),
    ]
