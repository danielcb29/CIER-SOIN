from django.shortcuts import render
from django.http import HttpResponseRedirect
from .cursoobserver import CursoObserver
from teacher.forms import LeaderTeacherForm
from .forms import CursoForm
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.

def listar_curos_area(request,area):
    observer = CursoObserver()
    curso_list,area_obj = observer.update(area)
    lt_form = LeaderTeacherForm(initial={'area_interes':area_obj})
    return render(request,'index.html',{'form':lt_form,'curso_list':curso_list})

#Funcionalidades con login
@login_required
@permission_required('curso.add_curso', login_url="/index")
def crear_curso(request):
    curso = CursoForm()
    exito = false
    if request.method=='POST':
        curso = CursoForm(request.POST)
        curso.save()
        exito = True
        curso = CursoForm()
    return render(request, 'crear_curso.html', {'form':CursoForm,'exito':exito} )
