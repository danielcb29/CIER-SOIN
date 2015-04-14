# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0010_teacher_area_interes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='departamento',
            field=models.CharField(default=b'Valle del Cauca', max_length=100, choices=[(b'Valle del Cauca', b'Valle del Cauca'), (b'Cauca', b'Cauca'), (b'Narino', b'Narino'), (b'Tolima', b'Tolima'), (b'Huila', b'Huila'), (b'Caqueta', b'Caqueta'), (b'Putumayo', b'Putumayo'), (b'Amazonas', b'Amazonas')]),
            preserve_default=True,
        ),
    ]
