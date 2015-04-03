# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0001_initial'),
        ('teacher', '0009_remove_teacher_area_interes'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='area_interes',
            field=models.ForeignKey(default=0, to='areas.Area'),
            preserve_default=False,
        ),
    ]
