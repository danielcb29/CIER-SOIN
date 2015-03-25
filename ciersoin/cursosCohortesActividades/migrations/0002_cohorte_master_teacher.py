# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cohorte',
            name='master_teacher',
            field=models.OneToOneField(to='teacher.MasterTeacher'),
            preserve_default=True,
        ),
    ]
