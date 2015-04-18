__author__ = 'alvaromartinez'
from teacher.models import LeaderTeacher
from cursosCohortesActividades.models import Curso,Actividad,Cohorte
from calificacionesCertificados.models import Calificacion,Certificado

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
    def reportarAprobReproCurso(self, mes):
        lts = LeaderTeacher.objects.all().order_by('departamento')
        cohorte_in_month = Cohorte.objects.filter(fecha_final__month=mes,estudiantes__in= lts)
        aproved = Certificado.objects.filter(cohorte__in = cohorte_in_month,tipo='Excelencia').count
        reporv = Certificado.objects.filter(cohorte__in = cohorte_in_month,tipo='Asistencia').count
        i = 0
        ap_percent = []
        rp_percent = []
        for ap in aproved:
            total = ap + reporv[i]
            ap_percent.append((ap/total)*100)
            rp_percent.append((reporv[i]/total)*100)
            i += 1

        return ap_percent,rp_percent
    #Definicion de la funcion para la generacion de reporte de notas de los estudiantes en un curso determinado
    def reportarNotasEstu(self, idCurso):
        return 0

    #Definicion de la funcion para la generacion de reporte de historico de los estudiantes que han ganado un curso
    def reportarHistoricoEstudi(self, idCurso):
        return 0

    #Definicion de la funcion para la generacion de reporte de datos de los estudiantes detallados y organizados por departamentos
    def reportarEstudianteDetPorDepartamento(self):
        return 0
