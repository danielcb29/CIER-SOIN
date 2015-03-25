from django.db import models

# Create your models here.
class HistoriaAcademica(models.Model):
    #Historial Academico
    universidad = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100)

class HistoriaLaboral(models.Model):
    #Historial laboral
    sede = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    grado = models.CharField(max_length=100)
    tiempo = models.IntegerField()
    tipoDeEnsenanza = models.CharField(max_length=100)
    anosDeExp = models.IntegerField()
