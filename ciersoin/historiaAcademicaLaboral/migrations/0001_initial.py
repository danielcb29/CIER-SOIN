# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaAcademica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('universidad', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('nivel', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoriaLaboral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sede', models.CharField(max_length=100)),
                ('institucion', models.CharField(max_length=100)),
                ('grado', models.CharField(max_length=100)),
                ('tiempo', models.IntegerField()),
                ('tipoDeEnsenanza', models.CharField(max_length=100)),
                ('anosDeExp', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
