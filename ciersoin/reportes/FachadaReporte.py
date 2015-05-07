__author__ = 'alvaromartinez'
from teacher.models import LeaderTeacher
from cursosCohortesActividades.models import Curso,Actividad,Cohorte,Actividad_Cohorte,Aspirante
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

#La	tienda	genera	unos	reportes	mensuales o	semestrales con	visualizaciones	graficas	de:

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
    #####ON TESTING########
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

