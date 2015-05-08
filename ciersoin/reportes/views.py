from django.shortcuts import render
import datetime
from .FachadaReporte import FachadaReporte
from cursosCohortesActividades.models import Curso
# Create your views here.
'''mon_str = {0:'Enero',1:'Febrero',2:'Marzo',3:'Abril',4:'Mayo',5:'Junio',6:'Julio',7:'Agosto',8:'Septiembre',9:'Ocutbre',10:'Noviembre',11:'Diciembre'}
        month = datetime.datetime.now().month
        mon_spanish = mon_str[month]'''
fachada = FachadaReporte()
def dashboards(request):
    regs = 'NIL'
    mes = 'No Seleccionado'
    periodo = 'No Seleccionado'
    year = 'No Seleccionado'
    #Cursos con bajo avance
    cursos_bajo = fachada.cursos_bajo_avance()
    if request.method == 'POST':
        mes = request.POST['mes']
        periodo=request.POST['periodo']
        year =request.POST['year']
        #Reporte aprobados y reporbados en un semestre
        aproved,reporv = fachada.reportarAprobReproCurso(periodo,year) #Aprobados y reporbados ordenados por dpto

        #Cantidad de asistentes a cursos
        lista_cursos,cantidad_asistentes = fachada.top10_max_estudiantes(mes,year)
        print 'EN VIEW'
        print lista_cursos,cantidad_asistentes
        #lista_cursos,cantidad_asistentes = ['Curso D','Curso MA'],[12,34]

        #Cantidad de lt por dpto en el mes
        numero_lt_region=fachada.total_lt_mes_region(mes,year)

        if len(aproved) == 0 and len(reporv) ==0 and len(cursos_bajo)==0 and len(numero_lt_region)==0 and len(lista_cursos)==0 and len(cantidad_asistentes)==0:
            regs='NO'
        else:
            regs='SI'

        return render(request,'reportes.html',{'mes':mes,'periodo':periodo,'year':year,'regs':regs,'lista_cursos':lista_cursos,'cantidad_asistentes':cantidad_asistentes,'ingreso_valle':numero_lt_region[0],'ingreso_cauca':numero_lt_region[1],'ingreso_narino':numero_lt_region[2],'ingreso_tolima':numero_lt_region[3],'ingreso_huila':numero_lt_region[4],'ingreso_caqueta':numero_lt_region[5],'ingreso_putumayo':numero_lt_region[6],'ingreso_amazonas':numero_lt_region[7],'porcentaje_gano':aproved,'porcentaje_perdio':reporv,'bajo_avance':cursos_bajo})
    return render(request,'reportes.html',{'mes':mes,'periodo':periodo,'year':year,'regs':regs,'bajo_avance':cursos_bajo})

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
        if len(cohortes_mes_dpto) == 0 and len(cohortes_mes_ganaron) ==0:
            regs='NO'
        else:
            regs='SI'
    return render(request,'listados.html',{'regs':regs,'mes':mes,'year':year,'curso':curso,'detalle_dpto':cohortes_mes_dpto,'cursos':cursos,'historico_mes':cohortes_mes_ganaron})