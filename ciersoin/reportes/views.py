from django.shortcuts import render
import datetime
from .FachadaReporte import FachadaReporte
from cursosCohortesActividades.models import Curso
# Create your views here.
fachada = FachadaReporte()
def dashboards(request):
    regs = 'NIL'
    mes = 'No Seleccionado'
    periodo = 'No Seleccionado'
    year = 'No Seleccionado'
    if request.method == 'POST':
        print 'Entramos'
        print request.POST['mes'],request.POST['periodo'],request.POST['year']
        #Reporte aprobados y reporbados en un semestre
        '''mon_str = {0:'Enero',1:'Febrero',2:'Marzo',3:'Abril',4:'Mayo',5:'Junio',6:'Julio',7:'Agosto',8:'Septiembre',9:'Ocutbre',10:'Noviembre',11:'Diciembre'}
        month = datetime.datetime.now().month
        mon_spanish = mon_str[month]'''
        #aproved,reporv = fachada.reportarAprobReproCurso(month) #Aprobados y reporbados ordenados por dpto

    return render(request,'reportes.html',{'mes':mes,'periodo':periodo,'year':year,'regs':regs})

def listados(request):
    cursos = Curso.objects.all()
    regs = 'NIL'
    mes = 'No Seleccionado'
    curso = 'No Seleccionado'
    year = 'No Seleccionado'
    cohortes_mes_dpto = []
    cohortes_mes_ganaron = []
    if request.method == 'POST':
        mes = request.POST['mes']
        curso = request.POST['curso']
        year = request.POST['year']
        cohortes_mes_dpto = fachada.list_est_curso_dpto(mes,curso,year) #Detalle de estudiantes de mes por dpto
        cohortes_mes_ganaron = fachada.hist_estud_ganaron(mes,curso,year) #Historico estudiantes ganaron curso
        if len(cohortes_mes_dpto) == 0 and len(cohortes_mes_ganaron):
            regs='NO'
        else:
            regs='SI'
    return render(request,'listados.html',{'regs':regs,'mes':mes,'year':year,'curso':curso,'detalle_dpto':cohortes_mes_dpto,'cursos':cursos,'historico_mes':cohortes_mes_ganaron})