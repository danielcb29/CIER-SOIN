# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_auto_20150325_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='historia_academica',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='historia_laboral',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='numeroIdentificacion',
        ),
        migrations.AddField(
            model_name='teacher',
            name='cedula',
            field=models.IntegerField(default=0, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
