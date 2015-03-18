from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cohorte(models.Model):
    pass

class Asistente(models.Model):
    #NOMBRE , APELLIDO , NOMBRE DE USUARIO , CONTRASEÑA, EMAIL : NO VAN PQ SE HEREDAN DEL MODELO USER DE DJANGO
    user = models.OneToOneField(User)
    #NO TIENE MAS ATRIBUTOS PQ SOLO ES UN MODELO QUE SE USARA PARA EL ROL ASISTENTE , NO NECESITAMOS MAS DATOS DE LA ASISTENTE SOLO ESOS PARA HACER EL LOGIN