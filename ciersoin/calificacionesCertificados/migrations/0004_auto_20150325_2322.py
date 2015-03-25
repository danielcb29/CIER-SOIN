# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calificacionesCertificados', '0003_auto_20150325_0058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calificacion',
            options={'permissions': (('ver_reportes', 'Visualizar reportes del sistema'),)},
        ),
    ]
