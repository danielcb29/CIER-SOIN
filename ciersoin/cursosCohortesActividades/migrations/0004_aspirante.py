# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_auto_20150329_0033'),
        ('cursosCohortesActividades', '0003_auto_20150325_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspirante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aceptado', models.BooleanField(default=False)),
                ('curso', models.ForeignKey(to='cursosCohortesActividades.Curso')),
                ('leader_teacher', models.ForeignKey(to='teacher.LeaderTeacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
