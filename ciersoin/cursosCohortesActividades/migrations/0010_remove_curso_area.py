# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0009_auto_20150401_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='area',
        ),
    ]
