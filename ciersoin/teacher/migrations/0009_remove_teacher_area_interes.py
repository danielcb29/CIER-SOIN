# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0008_auto_20150401_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='area_interes',
        ),
    ]
