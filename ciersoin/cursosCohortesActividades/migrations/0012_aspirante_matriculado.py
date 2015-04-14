# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0011_curso_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='aspirante',
            name='matriculado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
