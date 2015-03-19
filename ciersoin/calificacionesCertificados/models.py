from django.db import models
from calificacionesCertificados.models import LeaderTeacher
from cursosCohortesActividades.models import Cohorte
# Create your models here.

class Certificado(models.Model):
    leader_teacher = models.ForeignKey(LeaderTeacher)

    #Choices de tipo
    ASISTIO='Asistio'
    PARTICIPO='Participo'
    EXCELENCIA='Excelencia'

    TIPO_CERTIFICADO_CHOICES = (
        (ASISTIO,'Asistio'),
        (PARTICIPO,'Participo'),
        (EXCELENCIA,'Excelencia'),
    )

    tipo = models.CharField(max_length=100,choices=TIPO_CERTIFICADO_CHOICES,default=ASISTIO)

    cohorte = models.ForeignKey(Cohorte)

class Calificacion(models.Model):
    notas = models.CharField(max_length=35)
    cohorte = models.ForeignKey(Cohorte)
    leader_teacher = models.ForeignKey(LeaderTeacher)
