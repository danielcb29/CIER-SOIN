# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(default=b'Taller', max_length=100, choices=[(b'Examen', b'Examen'), (b'Taller', b'Taller'), (b'Exposicion', b'Exposicion'), (b'Lectura', b'Lectura')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cohorte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_cohorte', models.IntegerField()),
                ('fecha_inicial', models.DateField()),
                ('fecha_final', models.DateField()),
                ('actividad', models.ManyToManyField(to='cursosCohortesActividades.Actividad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('area', models.CharField(default=b'Matematicas', max_length=100, choices=[(b'Matematicas', b'Matematicas'), (b'Ciencias', b'Ciencias'), (b'Literatura', b'Literatura'), (b'Artes', b'Artes'), (b'Musica', b'Musica')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cohorte',
            name='curso',
            field=models.OneToOneField(to='cursosCohortesActividades.Curso'),
            preserve_default=True,
        ),
    ]
