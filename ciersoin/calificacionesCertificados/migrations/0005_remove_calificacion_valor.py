# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calificacionesCertificados', '0004_auto_20150325_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificacion',
            name='valor',
        ),
    ]
