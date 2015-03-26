# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_auto_20150326_2304'),
        ('historiaAcademicaLaboral', '0002_auto_20150326_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historialaboral',
            old_name='anosDeExp',
            new_name='anos_exp',
        ),
        migrations.RenameField(
            model_name='historialaboral',
            old_name='tipoDeEnsenanza',
            new_name='tipo_ensenanza',
        ),
        migrations.AddField(
            model_name='historiaacademica',
            name='teacher',
            field=models.OneToOneField(default=0, to='teacher.Teacher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historialaboral',
            name='teacher',
            field=models.OneToOneField(default=0, to='teacher.Teacher'),
            preserve_default=False,
        ),
    ]
