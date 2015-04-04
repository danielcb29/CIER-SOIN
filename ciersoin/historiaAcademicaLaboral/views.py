from django.shortcuts import render
from .forms import HistoriaAcademicaForm,HistoriaLaboralForm
#from teacher.teacherfactory import TeacherFactory
from django.contrib.auth.decorators import login_required,permission_required
from .models import HistoriaAcademica,HistoriaLaboral
from django.http import HttpResponseRedirect
# Create your views here.
@login_required
def nueva_academica(request):
    form_ha = HistoriaAcademicaForm()
    teacher_id = request.user.id
    exito = False
    if request.method == 'POST':
        form_ha = HistoriaAcademicaForm(request.POST)
        if form_ha.is_valid():
            form_ha.save()
            exito = True
            form_ha=HistoriaAcademicaForm()
    return render(request,'historia_academica.html',{'form':form_ha,'teacher_id':teacher_id,'exito':exito})

@login_required
def nueva_laboral(request):
    form_ha = HistoriaLaboralForm()
    teacher_id = request.user.id
    exito = False
    if request.method == 'POST':
        form_ha = HistoriaLaboralForm(request.POST)
        if form_ha.is_valid():
            form_ha.save()
            exito = True
            form_ha = HistoriaLaboralForm()
    return render(request,'historia_laboral.html',{'form':form_ha,'teacher_id':teacher_id,'exito':exito})

@login_required
def editar_ha(request,id):
    pass

@login_required
def eliminar_ha(request,id):
    ha = HistoriaAcademica.objects.get(id=id)
    if ha.activo:
        ha.activo=False
    else:
        ha.activo=True
    ha.save()
    return HttpResponseRedirect('/teacher/configuracion')

@login_required
def editar_hl(request,id):
    pass

@login_required
def eliminar_hl(request,id):
    hl= HistoriaLaboral.objects.get(id=id)
    if hl.activo:
        hl.activo=False
    else:
        hl.activo=True
    hl.save()
    return HttpResponseRedirect('/teacher/configuracion')