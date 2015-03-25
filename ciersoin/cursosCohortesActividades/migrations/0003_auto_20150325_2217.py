# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20150325_2217'),
        ('cursosCohortesActividades', '0002_cohorte_master_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='curso',
            field=models.OneToOneField(default=0, to='cursosCohortesActividades.Curso'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cohorte',
            name='estudiantes',
            field=models.ManyToManyField(to='teacher.LeaderTeacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cohorte',
            name='periodo',
            field=models.CharField(default=b'I:Feb-Jun', max_length=100, choices=[(b'I:Feb-Jun', b'I:Feb-Jun'), (b'II:Agos-Dic', b'II:Agos-Dic')]),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='cohorte',
            unique_together=set([('numero_cohorte', 'periodo', 'fecha_inicial')]),
        ),
    ]
