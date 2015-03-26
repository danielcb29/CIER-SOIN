# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historiaAcademicaLaboral', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaacademica',
            name='nivel',
            field=models.CharField(default=b'Pregrado', max_length=100, choices=[(b'Pregrado', b'Pregrado'), (b'Maestria', b'Maestria'), (b'Doctorado', b'Doctorado'), (b'PosDoctorado', b'PosDoctorado')]),
            preserve_default=True,
        ),
    ]
