from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MasterTeacher(models.Model):
    #NOMBRE , APELLIDO , NOMBRE DE USUARIO , CONTRASEÑA, EMAIL : NO VAN PQ SE HEREDAN DEL MODELO USER DE DJANGO
    user = models.OneToOneField(User)