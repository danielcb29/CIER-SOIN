# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0011_curso_area'),
    ]

    operations = [

        migrations.AlterField(
            model_name='actividad',
            name='curso',
            field=models.ForeignKey(to='cursosCohortesActividades.Curso'),
            preserve_default=True,
        ),
    ]
