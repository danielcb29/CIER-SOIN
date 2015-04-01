# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0006_auto_20150401_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 1, 16, 34, 47, 787954)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cohorte',
            name='curso',
            field=models.ForeignKey(to='cursosCohortesActividades.Curso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cohorte',
            name='master_teacher',
            field=models.ForeignKey(to='teacher.MasterTeacher'),
            preserve_default=True,
        ),
    ]
