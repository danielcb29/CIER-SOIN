from django.shortcuts import render
from .estadoCurso import Contexto,EstadoCursoExiste,EstadoCursoNoExiste
from teacher.models import MasterTeacher,LeaderTeacher
from cursosCohortesActividades.models import Cohorte,Actividad_Cohorte,Actividad,Aspirante
from django.contrib.auth.decorators import login_required,permission_required
from .models import Calificacion
from django.http import Http404

# Create your views here.

@login_required
@permission_required('teacher.ver_calificaciones',login_url="/index")
#Metodo que permite visualizar las calificaciones de un lt
def consultar_calificaciones(request):
    lt = LeaderTeacher.objects.get(id=request.user.id)
    cohortes = Cohorte.objects.filter(estudiantes=lt,activo=True)
    for c in cohortes:
        aspirante = Aspirante.objects.filter(leader_teacher=lt,curso=c.curso)
        if len(aspirante) !=0:
            c.asistencia=aspirante[0].asistencia
        else:
            c.asistencia=False
        actividades = Actividad_Cohorte.objects.filter(cohorte=c)
        for a in actividades:
            calif = Calificacion.objects.get(actividad_cohorte=a,leader_teacher=lt)
            if float(calif.valor) != -1.0:
                a.nota = calif
            else:
                a.nota = 'NIL'
        c.actividades = actividades
        if len(actividades) == 0:
            c.has_act = False
        else:
            c.has_act = True
    return render(request,'visualizar_calificaciones.html',{'cohortes':cohortes})

@login_required
@permission_required('teacher.ver_calificaciones',login_url="/index")
# Metodo para la generacion de certificados
def generar_Certificado(request, id_cohor,id_teach):
    contexto = Contexto()
    if contexto.existe_certficiado(id_teach,id_cohor):
        existe = EstadoCursoExiste()
        cert = existe.generarCertificado(id_teach,id_cohor)
        return render(request,'certificado.html',{'certificado':cert})
    else:
        existe = EstadoCursoNoExiste()
        if existe.posible(id_teach,id_cohor):
            cert = existe.generarCertificado(id_teach,id_cohor)
            return render(request,'certificado.html',{'certificado':cert})
        else:
            repro = True
            lt = LeaderTeacher.objects.get(id=request.user.id)
            cohortes = Cohorte.objects.filter(estudiantes=lt,activo=True)
            for c in cohortes:
                actividades = Actividad_Cohorte.objects.filter(cohorte=c)
                for a in actividades:
                    calif = Calificacion.objects.get(actividad_cohorte=a,leader_teacher=lt)
                    if float(calif.valor) != -1.0:
                        a.nota = calif
                    else:
                        a.nota = 'NIL'
                c.actividades = actividades
            return render(request,'visualizar_calificaciones.html',{'repro':repro,'cohortes':cohortes})

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
        if float(calificacion.valor) != -1.0:
            est.val  =calificacion
        else:
            est.val = 0
    if request.method=='POST':
        for est in estudiantes:
            calificacion = Calificacion.objects.get(actividad_cohorte = actividades_cohorte, leader_teacher = est)
            valor = request.POST[str(est.id)]
            if float(valor) >= 0.0 and float(valor) <= 5.0:
                calificacion.valor = valor
            else:
                return Http404('Error con el valor de las notas, Esta ingresando al backend desde otra fuente?')
            calificacion.save()
            exito = True
            est.val = calificacion
    return render(request,'calificar_actividad.html',{'cohorte':cohorte,'actividad':actividad,'estudiantes':estudiantes,'exito':exito})

@login_required
@permission_required('teacher.anadir_calificaciones',login_url="/index")
def listar_calificaciones(request):
    mt = MasterTeacher.objects.get(id=request.user.id)
    cohortes = Cohorte.objects.filter(master_teacher=mt,activo=True)
    for c in cohortes:
        actividades = Actividad_Cohorte.objects.filter(cohorte=c)
        estudiantes = c.estudiantes.all()
        for lt in estudiantes:
            calificaciones = []
            for a in actividades:
                calif = Calificacion.objects.get(actividad_cohorte=a,leader_teacher=lt)
                if float(calif.valor) != -1.0:
                    calificaciones.append(calif.valor)
                else:
                    calificaciones.append('NIL')
            lt.calificaciones = calificaciones
        c.actividades = actividades
        c.est = estudiantes
    return render(request,'listar_calificaciones.html',{'cohortes':cohortes})

@login_required
@permission_required('teacher.anadir_calificaciones',login_url="/index")
def ingresar_asistencia(request,id_cohor):
    cohorte = Cohorte.objects.get(id=id_cohor)
    estudiantes = cohorte.estudiantes.all()
    exito=False
    curso = cohorte.curso
    for es in estudiantes:
        aspirante = Aspirante.objects.get(curso=curso,leader_teacher=es)
        es.check = aspirante.asistencia
    if request.method=='POST':
        for es in estudiantes:
            aspirante = Aspirante.objects.get(curso=curso,leader_teacher=es)
            if str(es.id) in request.POST:
                aspirante.asistencia=True
                es.check=True
            else:
                aspirante.asistencia=False
                es.check=False
            aspirante.save()
            exito = True
    return render(request,'calificar_asistencia.html',{'cohorte':cohorte,'estudiantes':estudiantes,'exito':exito})



