__author__ = 'alvaromartinez'
from teacher.models import LeaderTeacher
from cursosCohortesActividades.models import Curso,Actividad,Cohorte,Actividad_Cohorte
from calificacionesCertificados.models import Calificacion,Certificado

class FachadaReporte():

#La	tienda	genera	unos	reportes	mensuales	en	forma	de	texto	en	tablas	de:

    #Detalle	de	estudiantes	en	un	curso	por	departamentos
    def list_est_curso_dpto(self,mes,curso,year):
        curso = Curso.objects.get(nombre=curso)
        cohortes = Cohorte.objects.filter(curso=curso,fecha_final__month=mes,fecha_final__year=year)
        for c in cohortes:
            c.est = c.estudiantes.all().order_by('departamento')
        return cohortes

    #Historico	de	estudiantes	que	hay	ganado	un	curso
    def hist_estud_ganaron(self,mes,curso,year):
        curso = Curso.objects.get(nombre=curso)
        cohortes = Cohorte.objects.filter(curso=curso,fecha_final__month=mes,fecha_final__year=year)
        for c in cohortes:
            c.cert = Certificado.objects.filter(cohorte=c)
        return cohortes

#La	tienda	genera	unos	reportes	mensuales o	semestrales con	visualizaciones	gráficas	de:

    #Definicion de la funcion para la generacion de reporte de asistentes por  un curso determinado
    def reportarAsistCurso(self, idCurso):
        pass

    #Definicion de la funcion para la generacion de reporte de docentes por departamento
    def reportarDocentePorDepart(self, idDepart):
        pass

    #Definicion de la funcion para la generacion de reporte de cursos con menos potencial de avance
    def reportarCursosMenosPotencial(self):
        pass

    #Definicion de la funcion para la generacion de reporte de Porcentaje de aprobados y reprobados en un curso determinado
    def reportarAprobReproCurso(self,periodo,year):
        lts = LeaderTeacher.objects.all().order_by('departamento')
        cohorte_in_semester = Cohorte.objects.filter(fecha_final__year=year,estudiantes__in= lts,periodo=periodo).distinct()
        array_act_cohor = []
        for coh in cohorte_in_semester:
            actvi = Actividad_Cohorte.objects.filter(cohorte=coh)
            array_act_cohor.append(actvi)

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
        pass

    #Definicion de la funcion para la generacion de reporte de historico de los estudiantes que han ganado un curso
    def reportarHistoricoEstudi(self, idCurso):
        pass

    #Definicion de la funcion para la generacion de reporte de datos de los estudiantes detallados y organizados por departamentos
    def reportarEstudianteDetPorDepartamento(self):
        pass
