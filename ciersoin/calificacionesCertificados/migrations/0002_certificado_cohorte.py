# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0001_initial'),
        ('calificacionesCertificados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificado',
            name='cohorte',
            field=models.ForeignKey(to='cursosCohortesActividades.Cohorte'),
            preserve_default=True,
        ),
    ]
