from django.shortcuts import render
import datetime
from .FachadaReporte import FachadaReporte
# Create your views here.
fachada = FachadaReporte()
def dashboards(request):
    mon_str = {0:'Enero',1:'Febrero',2:'Marzo',3:'Abril',4:'Mayo',5:'Junio',6:'Julio',7:'Agosto',8:'Septiembre',9:'Ocutbre',10:'Noviembre',11:'Diciembre'}
    month = datetime.datetime.now().month
    mon_spanish = mon_str[month]
    aproved,reporv = fachada.reportarAprobReproCurso(month) #Aprobados y reporbados ordenados por dpto
    return render(request,'reportes.html',{'mes':mon_spanish})

def listados(request):
    return render(request,'listados.html',{})