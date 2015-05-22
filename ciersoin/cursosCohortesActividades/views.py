from django.shortcuts import render
from django.http import HttpResponseRedirect
from .cursoobserver import CursoObserver
from teacher.forms import LeaderTeacherForm
from .models import Curso, Actividad, Cohorte, Aspirante
from .forms import CursoForm, ActividadForm, CohorteForm
from teacher.models import LeaderTeacher
from .models import Curso, Actividad,Actividad_Cohorte
from .forms import CursoForm, ActividadForm
from calificacionesCertificados.models import Calificacion
from django.contrib.auth.decorators import login_required,permission_required
import datetime
# Create your views here.

def listar_curos_area(request,area):
    observer = CursoObserver()
    curso_list,area_obj = observer.update(area)
    lt_form = LeaderTeacherForm(initial={'area_interes':area_obj})
    lt_registrados = LeaderTeacher.objects.all().count()
    return render(request,'index.html',{'form':lt_form,'curso_list':curso_list,'total_lt':lt_registrados})

#Funcionalidades con login0
@login_required
@permission_required('cursosCohortesActividades.add_curso', login_url="/index")
def crear_curso(request):
    curso = CursoForm()
    exito = False
    if request.method=='POST':
        curso = CursoForm(request.POST)
        if curso.is_valid():
            curso.save()
            exito = True
            curso = CursoForm()
    return render(request, 'crear_curso.html', {'form':curso,'exito':exito} )

@login_required
@permission_required('cursosCohortesActividades.add_curso', login_url="/index")
def listar_curso(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {'cursos':cursos})

@login_required
@permission_required('cursosCohortesActividades.change_curso', login_url="/index")
def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if curso.activo:
        curso.activo=False
    else:
        curso.activo=True
    curso.save()
    return HttpResponseRedirect("/cursos/listarcursos")

@login_required
@permission_required('cursosCohortesActividades.change_curso', login_url="/index")
def editar_curso(request, id_curso):
    cursos = Curso.objects.all()
    curso = Curso.objects.get(pk = id_curso)
    form_edicion = CursoForm(instance=curso, initial=curso.__dict__)
    if request.method == 'POST':
        form_edicion = CursoForm(
            request.POST, instance=curso, initial=curso.__dict__)
        if form_edicion.has_changed():
            if form_edicion.is_valid():
                form_edicion.save()
                return HttpResponseRedirect("/cursos/listarcursos")
        else:
            return HttpResponseRedirect("/cursos/listarcursos")
    return render(request, 'listar_cursos.html', {'cursos': cursos, 'edicion': True, 'form_edicion': form_edicion})


@login_required
@permission_required('cursosCohortesActividades.add_actividad',login_url='index')
def crear_actividad(request):
    actividad = ActividadForm()
    exito = False
    if request.method =='POST':
        actividad = ActividadForm(request.POST)
        if actividad.is_valid():
            actividad.save()
            exito = True
            actividad = ActividadForm()
    return render(request, 'crear_actividades.html', {'form':ActividadForm, 'exito':exito})



@login_required
@permission_required('cursosCohortesActividades.add_cohorte',login_url='index')
def listar_cohorte(request):
    cohortes = Cohorte.objects.all()
    return render(request, 'listar_cohortes.html', {'cohortes':cohortes})


@login_required
@permission_required('cursosCohortesActividades.add_actividades', login_url="/index")
def listar_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, 'listar_actividades.html', {'actividades':actividades})

@login_required
@permission_required('cursosCohortesActividades.change_actividad', login_url="/index")
def editar_actividad(request, id_actividad):
    actividades = Actividad.objects.all()
    actividad = Actividad.objects.get(pk = id_actividad)
    form_edicion = ActividadForm(instance=actividad, initial=actividad.__dict__)
    if request.method == 'POST':
        form_edicion = ActividadForm(
            request.POST, instance=actividad, initial=actividad.__dict__)
        if form_edicion.has_changed():
            if form_edicion.is_valid():
                form_edicion.save()
                return HttpResponseRedirect("/actividades/listar")
        else:
            return HttpResponseRedirect("/actividades/listar")
    return render(request, 'listar_actividades.html', {'actividades': actividades, 'edicion': True, 'form_edicion': form_edicion})


@login_required
@permission_required('cursosCohortesActividades.add_actividad',login_url='index')
def eliminar_actividad(request, id):
    actividad = Actividad.objects.get(id=id)
    if actividad.activo:
        actividad.activo=False
    else:
        actividad.activo=True
    actividad.save()
    return HttpResponseRedirect("/actividades/listar")

#Funcionalidades adicionales de la matricula

@login_required
@permission_required('cursosCohortesActividades.add_cohorte',login_url='index')
def crear_cohorte_paso_curso(request):
    cursos = Curso.objects.all()
    return render(request,'crear_cohorte_paso_curso.html',{'curso_list':cursos})

@login_required
@permission_required('cursosCohortesActividades.add_cohorte',login_url='index')
def crear_cohorte_estudiantes(request,nombre_curso):
    curso = Curso.objects.get(nombre=nombre_curso)
    cohorte = CohorteForm(initial={'curso':curso})
    estudiantes = [asp.leader_teacher for asp in Aspirante.objects.filter(curso=curso,matriculado=False,aceptado=True)]
    print (estudiantes)
    if request.method =='POST':
        cohorte = CohorteForm(request.POST)
        print (cohorte.errors)
        if cohorte.is_valid():
            cohorteCread = cohorte.save()
            leader_teachers = cohorteCread.estudiantes.all()
            for leader_teacher_coho in leader_teachers:
                aspirante_cohorte = Aspirante.objects.get(leader_teacher=leader_teacher_coho,curso=cohorteCread.curso)
                aspirante_cohorte.matriculado = True
                aspirante_cohorte.save()
            return HttpResponseRedirect('/cohortes/actividades/'+str(cohorteCread.id))
    return render(request, 'crear_cohorte_paso_estudiantes.html', {'form':cohorte, 'estudiantes':estudiantes,'curso':curso})

@login_required
@permission_required('cursosCohortesActividades.add_cohorte',login_url='index')
def crear_cohorte_actividades(request,id_cohorte):
    cohorte = Cohorte.objects.get(id=id_cohorte)
    actividades = Actividad.objects.filter(curso=cohorte.curso)
    exito=False
    if request.method=='POST':
        for act in actividades:
            if str(act.id) in request.POST:
                s_in= request.POST['fecha_in_'+str(act.id)]
                d_in = datetime.date(int(s_in[6:]),int(s_in[:2])-1,int(s_in[3:5]))
                s_fn = request.POST['fecha_fin_'+str(act.id)]
                d_fn = datetime.date(int(s_fn[6:]),int(s_fn[:2])-1,int(s_fn[3:5]))
                actividad_coh = Actividad_Cohorte(cohorte=cohorte,actividad=act,fecha_inicial=d_in,fecha_entrega=d_fn)
                actividad_coh.save()
                for es in cohorte.estudiantes.all():
                    cal = Calificacion()
                    cal.actividad_cohorte= actividad_coh
                    cal.leader_teacher = es
                    cal.save()
                act.check=True
                act.f_in = s_in
                act.f_fn = s_fn
        exito=True
    return render(request,'crear_cohorte_paso_actividades.html',{'actividades':actividades,'exito':exito})

@login_required
@permission_required('cursosCohortesActividades.change_cohorte',login_url='index')
def eliminar_cohorte(request, id):
    cohorte = Cohorte.objects.get(id=id)
    if cohorte.activo:
        cohorte.activo=False
    else:
        cohorte.activo=True
    cohorte.save()
    return HttpResponseRedirect("/cohortes/listarcohorte")

@login_required
@permission_required('cursosCohortesActividades.change_cohorte', login_url="/index")
def editar_cohorte(request, id_coho):
    cohorte = Cohorte.objects.get(pk = id_coho)
    estudiantes_cohor = cohorte.estudiantes.all()
    estudiantes = [asp.leader_teacher for asp in Aspirante.objects.filter(curso=cohorte.curso,aceptado=True)]
    for es in estudiantes:
        if es in estudiantes_cohor:
            es.selected=True
        else:
            es.selected=False
    form_edicion = CohorteForm(instance=cohorte, initial=cohorte.__dict__)
    if request.method == 'POST':
        form_edicion = CohorteForm(
            request.POST, instance=cohorte, initial=cohorte.__dict__)
        if form_edicion.has_changed():
            if form_edicion.is_valid():
                new_coh = form_edicion.save()
                new_estudiantes = new_coh.estudiantes.all()
                for es in estudiantes_cohor :
                    if es not in new_estudiantes:
                        aspirante = Aspirante.objects.get(leader_teacher=es,curso=new_coh.curso)
                        aspirante.matriculado=False
                        aspirante.save()
                return HttpResponseRedirect("/cohortes/editarcohorte/actividades/"+str(cohorte.id))
        else:
            return HttpResponseRedirect("/cohortes/editarcohorte/actividades/"+str(cohorte.id))
    return render(request, 'crear_cohorte_paso_estudiantes.html', {'form': form_edicion,'estudiantes':estudiantes,'curso':cohorte.curso})

@login_required
@permission_required('cursosCohortesActividades.change_cohorte', login_url="/index")
def editar_cohorte_actividad(request, id_coho):
    cohorte = Cohorte.objects.get(id=id_coho)
    actividades = Actividad.objects.filter(curso=cohorte.curso)
    actividades_cohor = [act_coh.actividad for act_coh in Actividad_Cohorte.objects.filter(cohorte=cohorte)]
    for ac in actividades:
        if ac in actividades_cohor:
            ac.check=True
            act_coh = Actividad_Cohorte.objects.get(actividad=ac,cohorte=cohorte)
            #ac.f_in = str(act_coh.fecha_inicial.month)+'/'+str(act_coh.fecha_inicial.day)+'/'+str(act_coh.fecha_inicial.year)
            #ac.f_fn = str(act_coh.fecha_entrega.month)+'/'+str(act_coh.fecha_entrega.day)+'/'+str(act_coh.fecha_entrega.year)
            #print ac.f_in,ac.f_fn
            ac.f_in = format_dates(str(act_coh.fecha_inicial.month)+'/'+str(act_coh.fecha_inicial.day)+'/'+str(act_coh.fecha_inicial.year))
            ac.f_fn = format_dates(str(act_coh.fecha_entrega.month)+'/'+str(act_coh.fecha_entrega.day)+'/'+str(act_coh.fecha_entrega.year))
        else:
            ac.check=False
    exito=False
    if request.method=='POST':
        array_new_act = []
        for ac in actividades:
            if str(ac.id) in request.POST:
                ex = Actividad_Cohorte.objects.filter(actividad=ac,cohorte=cohorte)
                s_in = request.POST['fecha_in_'+str(ac.id)]
                d_in = datetime.date(int(s_in[6:]),int(s_in[:2])-1,int(s_in[3:5]))
                s_fn = request.POST['fecha_fin_'+str(ac.id)]
                d_fn = datetime.date(int(s_fn[6:]),int(s_fn[:2])-1,int(s_fn[3:5]))
                if len(ex) != 0:
                    if ex[0].fecha_inicial != d_in or ex[0].fecha_entrega != d_fn:
                        ex[0].fecha_inicial=d_in
                        ex[0].fecha_entrega=d_fn
                        ex[0].save()
                        array_new_act.append(ex[0])
                else:
                    actividad_coh = Actividad_Cohorte(cohorte=cohorte,actividad=ac,fecha_inicial=d_in,fecha_entrega=d_fn)
                    actividad_coh.save()
                    for es in cohorte.estudiantes.all():
                        cal = Calificacion()
                        cal.actividad_cohorte= actividad_coh
                        cal.leader_teacher = es
                        cal.save()
                    array_new_act.append(actividad_coh)
                ac.check=True
                ac.f_in = s_in
                ac.f_fn = s_fn
                exito=True
        for a_ch in actividades_cohor:
            if a_ch not in array_new_act:
                actividad_cohorte = Actividad_Cohorte.objects.get(actividad=a_ch,cohorte=cohorte)
                for e in cohorte.estudiantes.all():
                    Calificacion.objects.get(leader_teacher=e,actividad_cohorte=actividad_cohorte).delete()
                actividad_cohorte.delete()
    return render(request,'crear_cohorte_paso_actividades.html',{'actividades':actividades,'exito_edit':exito})

def format_dates(date):
    if date[1:2] == '/':
        date = '0' + date
    if date[4:5] == '/':
        date = date[:3] + '0' + date[3:]
    return date

