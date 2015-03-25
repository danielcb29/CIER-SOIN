from django.db import models
from django.contrib.auth.models import User
from historiaAcademicaLaboral.models import HistoriaAcademica,HistoriaLaboral
# Create your models here.
# Modelo para Master Teacher, con datos personales, historia laboral e historial academico

class Teacher(User):
    #Zonas
    URBANA='Urbana'
    URBANAMARG='Urbana Marginal'
    RURAL='Rural'
    RURALDIFACC = 'Rural de dificil acceso'

    #Tipo de ensenanza

    ACADEMICA = 'Academica'
    TECNICA = 'Tecnica'

    TIPO_ZONA_CHOICES = (
        (URBANA,'Urbana'),
        (URBANAMARG, 'Urbana Marginal'),
        (RURAL,'Rural'),
        (RURALDIFACC, 'Rural de dificil acceso'),
    )

    TIPO_ENSENANZA_CHOICES = (
        (ACADEMICA, 'Academica'),
        (TECNICA, 'Tecnica'),
    )

    #Datos personales
    #NOMBRE , APELLIDO , NOMBRE DE USUARIO , CONTRASEnA, EMAIL : NO VAN PQ SE HEREDAN DEL MODELO USER DE DJANGO

    numeroIdentificacion = models.IntegerField()
    direccion = models.CharField(max_length=100)
    municipio  = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    zona = models.CharField(max_length=100, choices=TIPO_ZONA_CHOICES,default=URBANA)

    historia_academica = models.ForeignKey(HistoriaAcademica) #Puede tener varios titulos academicos
    historia_laboral = models.ForeignKey(HistoriaLaboral) #Puede tener varios historiales laborares


