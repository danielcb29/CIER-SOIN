__author__ = 'alvaromartinez'
from teacher.models import LeaderTeacher
from cursosCohortesActividades.models import Curso,Actividad,Cohorte,Actividad_Cohorte,Aspirante
from calificacionesCertificados.models import Calificacion,Certificado
import os,datetime

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

#La	tienda	genera	unos	reportes	mensuales o	semestrales con	visualizaciones	graficas	de:

    #Cursos	con	menos	potencial	de	avance
    def cursos_bajo_avance(self):
        os.environ['TZ'] = 'America/Bogota'
        calificaciones = Calificacion.objects.filter(valor=-1.0).distinct('actividad_cohorte')
        cursos_atrasados  =[]
        for cal in calificaciones:
            cohorte = cal.actividad_cohorte.cohorte
            now = datetime.date.today()
            if len(cursos_atrasados) == 5:
                break
            elif cohorte.fecha_final < now:
                cohorte.curso.dias = (now - cohorte.fecha_final).days
                cursos_atrasados.append(cohorte.curso)
        return cursos_atrasados


    #####ON TESTING########
    def ordenar_cursos(self,cursos):
        a = []
        b = []
        for c in cursos:
            a.append(c.nombre)
            b.append(c.total)
        return a,b

    #Cursos	con	mayor	numero	de	asistentes en	el	mes	(Top	10)
    #####ON TESTING########
    def top10_max_estudiantes(self,mes,year):
        cursos = Curso.objects.all()
        for c in cursos:
            cohortes = Cohorte.objects.filter(fecha_inicial__month__lte= mes, fecha_final__month__gte = mes, fecha_inicial__year__lte=year, fecha_final__year__gte=year,curso=c)
            total = 0
            for ch in cohortes:
                total += ch.estudiantes.all().count()
            c.total = total
        nombres,valores = self.ordenar_cursos(cursos)
        return nombres,valores

    #Definicion de la funcion para la generacion de reporte de Porcentaje de aprobados y reprobados en un curso determinado
    def reportarAprobReproCurso(self,periodo,year):
        departamentos = ["Valle", "Cauca", "Narino", "Tolima", "Huila", "Caqueta", "Putumayo","Amazonas"]
        cohortes = Cohorte.objects.filter(periodo=periodo,fecha_final__year=year)
        ganaron = []
        perdieron = []
        for dpto in departamentos:
            paso = 0
            reprob = 0
            for ch in cohortes:
                est = ch.estudiantes.filter(departamento=dpto)
                act = Actividad_Cohorte.objects.filter(cohorte=ch)
                for e in est:
                    definitiva = 0
                    for a in act:
                        calificacion = float(Calificacion.objects.get(leader_teacher=e,actividad_cohorte=a).valor)
                        #Que pasa si el curso va atrasao?, se le pone 0

                        if calificacion == -1.0:
                            definitiva+=0.0
                        else:
                            definitiva+=calificacion
                    definitiva /= len(act)
                    print definitiva
                    if definitiva <= 2.5:
                        reprob+=1
                    else:
                        paso+=1
            ganaron.append(paso )
            perdieron.append(reprob)
        return ganaron,perdieron

    #Numero	de	docentes	estudiantes	que	han	llegado	en	el	mes	de	cada	departamento	de	la	region
    def total_lt_mes_region(self,mes,year):
        departamentos = ["Valle", "Cauca", "Narino", "Tolima", "Huila", "Caqueta", "Putumayo","Amazonas"]
        cohortes = Cohorte.objects.filter(fecha_inicial__month=mes,fecha_inicial__year=year)
        numero = []
        for dpto in departamentos:
            total=0
            for ch in cohortes:
                total += ch.estudiantes.filter(departamento=dpto).count()
            numero.append(total)
        return numero

