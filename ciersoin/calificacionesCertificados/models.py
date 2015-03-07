from django.db import models
from calificacionesCertificados import LeaderTeacher
from cursosCohortesActividades import Cohorte
# Create your models here.

class Certificado(models.Model):
    leader_teacher = models.ForeignKey(LeaderTeacher)

    #Choices de tipo
    ASISTIO='AS'
    PARTICIPO='PA'
    EXCELENCIA='EX'

    TIPO_CERTIFICADO_CHOICES = (
        (ASISTIO,'Asistio'),
        (PARTICIPO,'Participo'),
        (EXCELENCIA,'EXCELENCIA'),
    )

    tipo = models.CharField(max_length=3,choices=TIPO_CERTIFICADO_CHOICES,default=ASISTIO)

    cohorte = models.ForeignKey(Cohorte)

class Calificacion(models.Model):
    notas = models.CharField(max_length=35)
    cohorte = models.ForeignKey(Cohorte)
    leader_teacher = models.ForeignKey(LeaderTeacher)
