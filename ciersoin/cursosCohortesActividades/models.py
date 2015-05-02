from django.db import models
from teacher.models import MasterTeacher,LeaderTeacher
import datetime
from areas.models import Area
# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    descripcion = models.TextField()
    SEIS = 6
    SIETE = 7
    SEMA_CHOICES = (
        (SEIS,6),
        (SIETE,7),
    )
    semanas = models.IntegerField(choices=SEMA_CHOICES,default=SEIS)
    area = models.ForeignKey(Area)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    # Tipos de actividades definidas por el sistema

    EXAMEN = 'Examen'
    TALLER = 'Taller'
    EXPOSICION = 'Exposicion'
    LECTURA = 'Lectura'

    TIPO_ACTIVIDAD_CHOICES = (
        (EXAMEN, 'Examen'),
        (TALLER, 'Taller'),
        (EXPOSICION, 'Exposicion'),
        (LECTURA, 'Lectura'),
    )

    tipo = models.CharField(max_length=100, choices=TIPO_ACTIVIDAD_CHOICES, default=TALLER)
    curso = models.ForeignKey(Curso) #Una actividad pertenece a un unico curso
    activo = models.BooleanField(default=True)
    #Se agrega fecha para saber si esta retrasada, Se elimina ya que es una abstraccion, las fechas se asignaran a cada actividad instanciada en cada cohorte
    #fecha_entrega = models.DateTimeField()
    def __str__(self):
        return self.nombre

class Cohorte(models.Model):
    numero_cohorte = models.IntegerField()
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    # Llaves foreneas de una cohorte, una para curso y otra su master teacher
    curso = models.ForeignKey(Curso)
    master_teacher = models.ForeignKey(MasterTeacher)

    PRIMER = 'I:Feb-Jun'
    SEGUNDO = 'II:Agos-Dic'

    PERIODO_COHORTE_CHOICES= (
        (PRIMER,'I:Feb-Jun'),
        (SEGUNDO,'II:Agos-Dic'),
    )

    periodo = models.CharField(max_length=100,choices=PERIODO_COHORTE_CHOICES,default=PRIMER)

    estudiantes = models.ManyToManyField(LeaderTeacher)

    #Relacion muchos a muchos con actividad se quita porque ya se creo una clase que las relaciona
    #actividad = models.ManyToManyField(Actividad)
    activo = models.BooleanField(default=True)
    class Meta:
        unique_together = ('numero_cohorte', 'periodo','fecha_inicial')

    def __str__(self):
        return self.curso.nombre+"-"+str(self.numero_cohorte)+":Periodo "+self.periodo

class Aspirante(models.Model):
    leader_teacher = models.ForeignKey(LeaderTeacher)
    curso = models.ForeignKey(Curso)
    aceptado = models.BooleanField(default=False)
    matriculado = models.BooleanField(default=False) #Para listar solo los que no han sido matriculados

    def __str__(self):
        return self.leader_teacher.get_full_name()

class Actividad_Cohorte(models.Model):
    actividad = models.ForeignKey(Actividad)
    cohorte = models.ForeignKey(Cohorte)
    fecha_inicial = models.DateTimeField()
    fecha_entrega = models.DateTimeField()

    def __str__(self):
        return self.actividad.nombre

