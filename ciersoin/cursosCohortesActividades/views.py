from django.shortcuts import render
from django.http import HttpResponseRedirect
from .cursoobserver import CursoObserver
from teacher.forms import LeaderTeacherForm
from .models import Curso, Actividad, Cohorte, Aspirante
from .forms import CursoForm, ActividadForm, CohorteForm
from teacher.models import LeaderTeacher
from .models import Curso, Actividad
from .forms import CursoForm, ActividadForm
from django.contrib.auth.decorators import login_required,permission_required
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
@permission_required('cursosCohortesActividades.change_cohorte', login_url="/index")
def editar_cohorte(request, id_actividad):
    cohortes = Cohorte.objects.all()
    cohorte = Cohorte.objects.get(pk = id_actividad)
    form_edicion = CohorteForm(instance=cohorte, initial=cohorte.__dict__)
    if request.method == 'POST':
        form_edicion = CohorteForm(
            request.POST, instance=cohorte, initial=cohorte.__dict__)
        if form_edicion.has_changed():
            if form_edicion.is_valid():
                form_edicion.save()
                return HttpResponseRedirect("/cohortes/listarcohorte")
        else:
            return HttpResponseRedirect("/cohortes/listarcohorte")
    return render(request, 'listar_cohortes.html', {'cohortes': cohortes, 'edicion': True, 'form_edicion': form_edicion})

@login_required
@permission_required('cursosCohortesActividades.add_cohorte',login_url='index')
def eliminar_cohorte(request, id):
    cohorte = Cohorte.objects.get(id=id)
    if cohorte.activo:
        cohorte.activo=False
    else:
        cohorte.activo=True
    cohorte.save()
    return HttpResponseRedirect("/cohortes/listarcohorte")

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

#Funcionalidades adicionales de la matricual

@login_required
@permission_required('cursosCohortesActividades.add_cohorte',login_url='index')
def crear_cohorte(request):
    cohorte = CohorteForm()
    exito = False
    if request.method =='POST':
        cohorte = CohorteForm(request.POST)
        print cohorte.errors
        if cohorte.is_valid():
            cohorteCread = cohorte.save()
            leader_teachers = cohorteCread.estudiantes.all()
            for leader_teacher_coho in leader_teachers:
                aspirante_cohorte = Aspirante.objects.get(leader_teacher=leader_teacher_coho,curso=cohorteCread.curso)
                aspirante_cohorte.matriculado = True
                aspirante_cohorte.save()
            exito = True
            cohorte = CohorteForm()
    return render(request, 'crear_cohorte_paso_estudiantes.html', {'form':cohorte, 'exito':exito})

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
    print estudiantes
    if request.method =='POST':
        cohorte = CohorteForm(request.POST)
        print cohorte.errors
        if cohorte.is_valid():
            cohorteCread = cohorte.save()
            leader_teachers = cohorteCread.estudiantes.all()
            for leader_teacher_coho in leader_teachers:
                aspirante_cohorte = Aspirante.objects.get(leader_teacher=leader_teacher_coho,curso=cohorteCread.curso)
                aspirante_cohorte.matriculado = True
                aspirante_cohorte.save()
    return render(request, 'crear_cohorte_paso_estudiantes.html', {'form':cohorte, 'estudiantes':estudiantes,'curso':curso})

def listar_actividades_cohorte(request):
    pass

