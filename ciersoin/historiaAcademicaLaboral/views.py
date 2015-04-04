from django.shortcuts import render
from .forms import HistoriaAcademicaForm,HistoriaLaboralForm
from django.contrib.auth.decorators import login_required,permission_required
from .models import HistoriaAcademica,HistoriaLaboral
from django.http import HttpResponseRedirect
from teacher.models import Teacher
from teacher.forms import TeacherEditForm
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
    editar = True
    ha = HistoriaAcademica.objects.get(id=id)
    ha_form = HistoriaAcademicaForm(instance=ha,initial=ha.__dict__)
    id_user = request.user.id
    teach = Teacher.objects.get(id=id_user)
    form = TeacherEditForm(instance=teach)
    historiasacademicas = HistoriaAcademica.objects.filter(teacher=teach)
    historiaslaborales = HistoriaLaboral.objects.filter(teacher=teach)
    exito_ha=False
    if request.method=='POST':
        form_nuevo = HistoriaAcademicaForm(request.POST,instance=ha,initial=ha.__dict__)
        if form_nuevo.has_changed():
            if form_nuevo.is_valid():
                form_nuevo.save()
                exito_ha = True
                editar=False
    return render(request,'edit_teach.html',{'editar':editar,'type':'Historia Academica','form_history':ha_form,'form':form,'historiaacademica':historiasacademicas,'historialaboral':historiaslaborales,'exito_ha':exito_ha})

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
    editar = True
    hl = HistoriaLaboral.objects.get(id=id)
    hl_form = HistoriaLaboralForm(instance=hl,initial=hl.__dict__)
    id_user = request.user.id
    teach = Teacher.objects.get(id=id_user)
    form = TeacherEditForm(instance=teach)
    historiasacademicas = HistoriaAcademica.objects.filter(teacher=teach)
    historiaslaborales = HistoriaLaboral.objects.filter(teacher=teach)
    exito_hl=False
    if request.method=='POST':
        form_nuevo = HistoriaLaboralForm(request.POST,instance=hl,initial=hl.__dict__)
        if form_nuevo.has_changed():
            if form_nuevo.is_valid():
                form_nuevo.save()
                exito_hl = True
                editar=False
    return render(request,'edit_teach.html',{'editar':editar,'type':'Historia Academica','form_history':hl_form,'form':form,'historiaacademica':historiasacademicas,'historialaboral':historiaslaborales,'exito_hl':exito_hl})

@login_required
def eliminar_hl(request,id):
    hl= HistoriaLaboral.objects.get(id=id)
    if hl.activo:
        hl.activo=False
    else:
        hl.activo=True
    hl.save()
    return HttpResponseRedirect('/teacher/configuracion')