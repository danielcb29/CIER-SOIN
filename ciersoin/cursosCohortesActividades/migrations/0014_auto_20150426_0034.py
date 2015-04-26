# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0013_auto_20150418_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad_Cohorte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicial', models.DateTimeField()),
                ('fecha_entrega', models.DateTimeField()),
                ('actividad', models.ForeignKey(to='cursosCohortesActividades.Actividad')),
                ('cohorte', models.ForeignKey(to='cursosCohortesActividades.Cohorte')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='fecha_entrega',
        ),
        migrations.RemoveField(
            model_name='cohorte',
            name='actividad',
        ),
    ]
