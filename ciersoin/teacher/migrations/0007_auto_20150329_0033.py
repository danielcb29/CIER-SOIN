# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_auto_20150326_2304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaderteacher',
            options={'permissions': (('ver_calificaciones', 'Puede ver calif descargar cert'), ('editar_datos_personales', 'Puede editar sus propios datos'), ('listar_LT', 'Se permite editar, activar , desactivar'), ('matricular_lt', 'Matricular estudiantes a cohortes'), ('terminar_datos_lt', 'Terminar datos lab y acad lt'))},
        ),
        migrations.AlterModelOptions(
            name='masterteacher',
            options={'permissions': (('anadir_calificaciones', 'Puede calificar cursos'), ('editar_datos_personales', 'Puede editar sus propios datos'), ('terminar_datos_mt', 'Terminar datos lab y acad mt'))},
        ),
        migrations.AddField(
            model_name='teacher',
            name='area_interes',
            field=models.CharField(default=b'Matematicas', max_length=100, choices=[(b'Matematicas', b'Matematicas'), (b'Ciencias', b'Ciencias'), (b'Literatura', b'Literatura'), (b'Artes', b'Artes'), (b'Musica', b'Musica')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='cedula',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
