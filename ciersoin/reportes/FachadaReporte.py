__author__ = 'alvaromartinez'
from teacher.models import LeaderTeacher
from cursosCohortesActividades import Cursos
from cursosCohortesActividades import Actividad
from calificacionesCertificados import Calificacion

class FachadaReporte():

    #Definicion de la funcion para la generacion de reporte de asistentes por  un curso determinado
    def reportarAsistCurso(self, idCurso):
        return 0

    #Definicion de la funcion para la generacion de reporte de docentes por departamento
    def reportarDocentePorDepart(self, idDepart):
        return 0

    #Definicion de la funcion para la generacion de reporte de cursos con menos potencial de avance
    def reportarCursosMenosPotencial(self):
        return 0

    #Definicion de la funcion para la generacion de reporte de Porcentaje de aprobados y reprobados en un curso determinado
    def reportarAprobReproCurso(self, idCurso):
        return 0

    #Definicion de la funcion para la generacion de reporte de notas de los estudiantes en un curso determinado
    def reportarNotasEstu(self, idCurso):
        return 0

    #Definicion de la funcion para la generacion de reporte de historico de los estudiantes que han ganado un curso
    def reportarHistoricoEstudi(self, idCurso):
        return 0

    #Definicion de la funcion para la generacion de reporte de datos de los estudiantes detallados y organizados por departamentos
    def reportarEstudianteDetPorDepartamento(self):
        return 0
