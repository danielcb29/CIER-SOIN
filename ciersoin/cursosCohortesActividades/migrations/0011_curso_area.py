# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0001_initial'),
        ('cursosCohortesActividades', '0010_remove_curso_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='area',
            field=models.ForeignKey(default=0, to='areas.Area'),
            preserve_default=False,
        ),
    ]
