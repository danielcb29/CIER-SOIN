from django.db import models
from django.contrib.auth.models import User
from areas.models import Area
# Create your models here.

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

    #Departamentos

    VALLE = 'Valle del Cauca'
    CAUCA = 'Cauca'
    NARINO = 'Narino'
    TOLIMA = 'Tolima'
    HUILA = 'Huila'
    CAQUETA = 'Caqueta'
    PUTUMAYO = 'Putumayo'
    AMAZONAS= 'Amazonas'

    DEP_CHOICES = (
        (VALLE , 'Valle del Cauca'),
        (CAUCA , 'Cauca'),
        (NARINO , 'Narino'),
        (TOLIMA , 'Tolima'),
        (HUILA , 'Huila'),
        (CAQUETA , 'Caqueta'),
        (PUTUMAYO , 'Putumayo'),
        (AMAZONAS , 'Amazonas'),
    )


    #Datos personales
    #NOMBRE , APELLIDO , NOMBRE DE USUARIO , CONTRASEnA, EMAIL : NO VAN PQ SE HEREDAN DEL MODELO USER DE DJANGO

    cedula = models.CharField(unique=True,max_length=100)
    direccion = models.CharField(max_length=100)
    municipio  = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100, choices = DEP_CHOICES , default= VALLE)
    zona = models.CharField(max_length=100, choices=TIPO_ZONA_CHOICES,default=URBANA)

    area_interes = models.ForeignKey(Area)


class LeaderTeacher(Teacher):
    class Meta:
        permissions = (
            # Permission identifier     human-readable permission name
            ("ver_calificaciones",               "Puede ver calif descargar cert"),
            ("editar_datos_personales",          "Puede editar sus propios datos"),
            ("listar_LT",                        "Se permite editar, activar , desactivar" ),
            ("matricular_lt",                    "Matricular estudiantes a cohortes" ),
            ("terminar_datos_lt",                "Terminar datos lab y acad lt" ),


        )

    def __str__(self):
        return self.get_full_name()

class MasterTeacher(Teacher):
    class Meta:
        permissions = (
            # Permission identifier     human-readable permission name
            ("anadir_calificaciones",            "Puede calificar cursos"),
            ("editar_datos_personales",          "Puede editar sus propios datos"),
            ("terminar_datos_mt",                "Terminar datos lab y acad mt" ),


        )

    def __str__(self):
        return self.get_full_name()

