from django.db import models
from django.contrib.auth.models import User
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

    #Datos personales
    #NOMBRE , APELLIDO , NOMBRE DE USUARIO , CONTRASEnA, EMAIL : NO VAN PQ SE HEREDAN DEL MODELO USER DE DJANGO

    cedula = models.IntegerField(unique=True)
    direccion = models.CharField(max_length=100)
    municipio  = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    zona = models.CharField(max_length=100, choices=TIPO_ZONA_CHOICES,default=URBANA)

    # Opciones para la area de un curso, faltan por definir mas areas

    MATEMATICA = 'Matematicas'
    CIENCIAS = 'Ciencias'
    LITERATURA = 'Literatura'
    ARTES = 'Artes'
    MUSICA = 'Musica'

    AREA_CURSO_CHOICES = (
        (MATEMATICA, 'Matematicas'),
        (CIENCIAS, 'Ciencias'),
        (LITERATURA, 'Literatura'),
        (ARTES, 'Artes'),
        (MUSICA, 'Musica'),
    )

    area_interes = models.CharField(max_length=100, choices=AREA_CURSO_CHOICES, default=MATEMATICA)



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

