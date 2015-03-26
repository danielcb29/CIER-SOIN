from django.db import models
from teacher.models import Teacher
# Create your models here.
class HistoriaAcademica(models.Model):
    PREGRADO = 'Pregrado'
    MAESTRIA = 'Maestria'
    DOCTORADO = 'Doctorado'
    POSDOC = 'PosDoctorado'
    NIVEL_CHOICES = (
        (PREGRADO , 'Pregrado'),
        (MAESTRIA , 'Maestria'),
        (DOCTORADO , 'Doctorado'),
        (POSDOC , 'PosDoctorado'),
    )

    #Historial Academico
    universidad = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100,choices=NIVEL_CHOICES,default=PREGRADO)
    teacher = models.OneToOneField(Teacher)#Pertenece a un unico profesor

class HistoriaLaboral(models.Model):
    #Historial laboral
    sede = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    grado = models.CharField(max_length=100)
    tiempo = models.IntegerField()
    tipo_ensenanza = models.CharField(max_length=100)
    anos_exp = models.IntegerField()
    teacher = models.OneToOneField(Teacher)#Pertenece a un unico profesor