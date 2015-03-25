# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('historiaAcademicaLaboral', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('numeroIdentificacion', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
                ('zona', models.CharField(default=b'Urbana', max_length=100, choices=[(b'Urbana', b'Urbana'), (b'Urbana Marginal', b'Urbana Marginal'), (b'Rural', b'Rural'), (b'Rural de dificil acceso', b'Rural de dificil acceso')])),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='MasterTeacher',
            fields=[
                ('teacher_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='teacher.Teacher')),
            ],
            options={
                'permissions': (('change_datos_personales', 'Puede cambiar sus datos personales'),),
            },
            bases=('teacher.teacher',),
        ),
        migrations.CreateModel(
            name='LeaderTeacher',
            fields=[
                ('teacher_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='teacher.Teacher')),
                ('matriculable', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('teacher.teacher',),
        ),
        migrations.AddField(
            model_name='teacher',
            name='historia_academica',
            field=models.ForeignKey(to='historiaAcademicaLaboral.HistoriaAcademica'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teacher',
            name='historia_laboral',
            field=models.ForeignKey(to='historiaAcademicaLaboral.HistoriaLaboral'),
            preserve_default=True,
        ),
    ]
