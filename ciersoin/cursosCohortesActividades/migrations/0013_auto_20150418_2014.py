# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0012_auto_20150418_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='curso',
            field=models.ForeignKey(to='cursosCohortesActividades.Curso'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aspirante',
            name='matriculado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
