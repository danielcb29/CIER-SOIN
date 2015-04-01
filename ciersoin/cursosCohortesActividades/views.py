from django.shortcuts import render
from django.http import HttpResponseRedirect
from .cursoobserver import CursoObserver
from teacher.forms import LeaderTeacherForm
# Create your views here.

def listar_curos_area(request,area):
    observer = CursoObserver()
    curso_list = observer.update(area)
    lt_form = LeaderTeacherForm()
    return render(request,'index.html',{'form':lt_form,'curso_list':curso_list})