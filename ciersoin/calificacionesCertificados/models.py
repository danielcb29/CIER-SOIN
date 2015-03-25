from django.db import models
from teacher.models import LeaderTeacher
from cursosCohortesActividades.models import Cohorte,Actividad
# Create your models here.

class Certificado(models.Model):
    leader_teacher = models.OneToOneField(LeaderTeacher)

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

    def __str__(self):
        return self.leader_teacher.get_full_name()+":"+self.tipo
#Una calificacion representa la abstraccion de una nota , una nota tiene un valor, una unica actividad a la cual pertenece y un unico estudiante
class Calificacion(models.Model):
    valor = models.CharField(max_length=35)
    actividad = models.OneToOneField(Actividad)
    leader_teacher = models.OneToOneField(LeaderTeacher)

    class Meta:
        permissions = (
            ("ver_reportes",  "Visualizar reportes del sistema"),
        )

    def __str__(self):
        return self.valor
