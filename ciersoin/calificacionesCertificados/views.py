from django.shortcuts import render
from .estadoCurso import Contexto
from teacher.models import MasterTeacher,LeaderTeacher
from cursosCohortesActividades.models import Cohorte,Actividad_Cohorte,Actividad
from django.contrib.auth.decorators import login_required,permission_required
from .models import Calificacion

# Create your views here.

@login_required
@permission_required('teacher.ver_calificaciones',login_url="/index")
#Metodo que permite visualizar las calificaciones de un lt
def consultar_calificaciones(request):
    lt = LeaderTeacher.objects.get(id=request.user.id)
    cohortes = Cohorte.objects.filter(estudiantes=lt,activo=True)
    for c in cohortes:
        actividades = Actividad_Cohorte.objects.filter(cohorte=c)
        for a in actividades:
            calif = Calificacion.objects.get(actividad_cohorte=a,leader_teacher=lt)
            if float(calif.valor) != -1.0:
                a.nota = calif
            else:
                a.nota = 'Nil'
        c.actividades = actividades
    return render(request,'visualizar_calificaciones.html',{'cohortes':cohortes})

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
    cohorte = Cohorte.objects.get(id=id_cohor)
    actividad = Actividad.objects.get(id=id_act)
    actividades_cohorte = Actividad_Cohorte.objects.get(actividad=actividad,cohorte=cohorte)
    estudiantes = cohorte.estudiantes.all()
    exito = False
    for est in estudiantes:
        calificacion = Calificacion.objects.get(actividad_cohorte = actividades_cohorte, leader_teacher = est)
        #print calificacion
        if float(calificacion.valor) != -1.0:
            est.val  =calificacion
        else:
            est.val = 0
    if request.method=='POST':
        for est in estudiantes:
            calificacion = Calificacion.objects.get(actividad_cohorte = actividades_cohorte, leader_teacher = est)
            calificacion.valor = request.POST[str(est.id)]
            calificacion.save()
            exito = True
    return render(request,'calificar_actividad.html',{'cohorte':cohorte,'actividad':actividad,'estudiantes':estudiantes,'exito':exito})





