# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosCohortesActividades', '0014_auto_20150426_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='semanas',
            field=models.IntegerField(default=6, choices=[(6, 6), (7, 7)]),
            preserve_default=True,
        ),
    ]
