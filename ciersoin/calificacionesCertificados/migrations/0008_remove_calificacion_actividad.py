# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calificacionesCertificados', '0007_auto_20150418_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificacion',
            name='actividad',
        ),
    ]
