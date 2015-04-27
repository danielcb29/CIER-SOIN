from django.shortcuts import render
from .estadoCurso import Contexto
from teacher.models import MasterTeacher
from cursosCohortesActividades.models import Cohorte,Actividad_Cohorte
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
def consultar_calificaciones(request):
    return render(request,'admin.html',{})

# Metodo para la generacion de certificados
def generar_Certificado(request, idTeacher):
    pass

@login_required
@permission_required('teacher.anadir_calificaciones',login_url="/index")
#Metodo que los MT usan para calificar los cursos
def calificar(request):
    mt = MasterTeacher.objects.get(id=request.user.id)
    cohortes = Cohorte.objects.filter(master_teacher=mt,activo=True)
    for c in cohortes:
        actividades = Actividad_Cohorte.objects.filter(cohorte=c)
        c.actividades = actividades
    return render(request,'ingresar_calificaciones.html',{'cohortes':cohortes})

@login_required
@permission_required('teacher.anadir_calificaciones',login_url="/index")
#Metodo para calificar una actvidad de una cohorte en particular
def ingresar_notas(request,id_cohor,id_act):
    pass





