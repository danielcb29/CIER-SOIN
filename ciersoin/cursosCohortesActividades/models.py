from django.db import models
from teacher.models import MasterTeacher
# Create your models here.

class Actividad(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()

    #Tipos de actividades definidas por el sistema

	EXAMEN = 'Examen'
	TALLER = 'Taller'
	EXPOSICION = 'Exposicion'
	LECTURA = 'Lectura'

	TIPO_ACTIVIDAD_CHOICES = (
		(EXAMEN,'Examen'),
		(TALLER,'Taller'),
		(EXPOSICION, 'Exposicion'),
		(LECTURA, 'Lectura'),
	)

	tipo = models.CharField(max_length=100, choices=TIPO_ACTIVIDAD_CHOICES, default=TALLER)

class Curso(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    #Opciones para la area de un curso, faltan por definir mas areas

    MATEMATICA = 'Matematicas'
    CIENCIAS = 'Ciencias'
    LITERATURA = 'Literatura'
    ARTES = 'Artes'
    MUSICA = 'Musica'

    AREA_CURSO_CHOICES = (
		(MATEMATICA,'Matematicas'),
		(CIENCIAS, 'Ciencias'),
		(LITERATURA, 'Literatura'),
		(ARTES, 'Artes'),
		(MUSICA,'Musica'),
	)

    area = models.CharField(max_length=100, choices=AREA_CURSO_CHOICES, default=MATEMATICA)

class Cohorte(models.Model):
    numero_cohorte = models.IntegerField()
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    #Llaves foreneas de una cohorte, una para curso y otra su master teacher
    curso = models.OneToOneField(Curso)
    master_teacher = models.OneToOneField(MasterTeacher)

    #Relacion muchos a muchos con actividad
    actividad = models.ManyToManyField(Actividad)


