from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Modelo para Master Teacher, con datos personales, historia laboral e historial academico
class MasterTeacher(models.Model):

    #Zonas
    URBANA='Urbana'
    URBANAMARG='Urbana Marginal'
    RURAL='Rural'
    RURALDIFACC = 'Rural de dificil acceso'

    #Tipo de enseñanza

    ACADEMICA = 'Académica'
    TECNICA = 'Técnica'

    TIPO_ZONA_CHOICES = (
        (URBANA,'Urbana'),
        (URBANAMARG, 'Urbana Marginal'),
        (RURAL,'Rural'),
        (RURALDIFACC, 'Rural de dificil acceso'),
    )

    TIPO_ENSENANZA_CHOICES = (
        (ACADEMICA, 'Académica'),
        (TECNICA, 'Técnica'),
    )

    #Datos personales
    #NOMBRE , APELLIDO , NOMBRE DE USUARIO , CONTRASEÑA, EMAIL : NO VAN PQ SE HEREDAN DEL MODELO USER DE DJANGO
    user = models.OneToOneField(User)
    numeroIdentificacion = models.IntegerField()
    direccion = models.CharField(max_length=100)
    municipio  = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    zona = models.CharField(max_length=100, choices=TIPO_ZONA_CHOICES,default=URBANA)

    #Historial laboral
    sede = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    grado = models.CharField(max_length=100)
    tiempo = models.IntegerField()
    tipoDeEnsenanza = models.CharField(max_length=100)
    anosDeExp = models.IntegerField()

    #Historial Academico
    universidad = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100)

