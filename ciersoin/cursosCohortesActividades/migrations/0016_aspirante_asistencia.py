# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0015_curso_semanas'),
    ]

    operations = [
        migrations.AddField(
            model_name='aspirante',
            name='asistencia',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
