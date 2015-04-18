from django.shortcuts import render
from django.http import HttpResponseRedirect
from .cursoobserver import CursoObserver
from teacher.forms import LeaderTeacherForm
from .models import Curso, Actividad
from .forms import CursoForm, ActividadForm
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.

def listar_curos_area(request,area):
    observer = CursoObserver()
    curso_list,area_obj = observer.update(area)
    lt_form = LeaderTeacherForm(initial={'area_interes':area_obj})
    return render(request,'index.html',{'form':lt_form,'curso_list':curso_list})

#Funcionalidades con login0
@login_required
@permission_required('curso.add_curso', login_url="/index")
def crear_curso(request):
    curso = CursoForm()
    exito = False
    if request.method=='POST':
        curso = CursoForm(request.POST)
        print curso.errors
        if curso.is_valid():
            curso.save()
            exito = True
            curso = CursoForm()
    return render(request, 'crear_curso.html', {'form':curso,'exito':exito} )

@login_required
@permission_required('curso.add_curso', login_url="/index")
def listar_curso(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {'cursos':cursos})

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if curso.activo:
        curso.activo=False
    else:
        curso.activo=True
    curso.save()
    return HttpResponseRedirect("/cursos/listarcursos")

@login_required
@permission_required('curso.change_curso', login_url="/index")
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
@permission_required('actividad.add_actividad',login_url='index')
def crear_actividad(request):
    actividad = ActividadForm()
    exito = False
    if request.method =='POST':
        actividad = ActividadForm(request.POST)
        print actividad.errors
        if actividad.is_valid():
            actividad.save()
            exito = True
            actividad = ActividadForm()
    return render(request, 'crear_actividades.html', {'form':ActividadForm, 'exito':exito})

def crear_cohorte(request):
    return render(request, 'crear_cohorte.html',{})
