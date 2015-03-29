# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historiaAcademicaLaboral', '0003_auto_20150326_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaacademica',
            name='teacher',
            field=models.ForeignKey(to='teacher.Teacher'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historialaboral',
            name='teacher',
            field=models.ForeignKey(to='teacher.Teacher'),
            preserve_default=True,
        ),
    ]
