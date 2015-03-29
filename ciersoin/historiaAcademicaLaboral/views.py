from django.shortcuts import render
from .forms import HistoriaAcademicaForm,HistoriaLaboralForm
#from teacher.teacherfactory import TeacherFactory
# Create your views here.

def nueva_academica(request):
    form_ha = HistoriaAcademicaForm()
    teacher_id = request.user.id
    exito = False
    if request.method == 'POST':
        form_ha = HistoriaAcademicaForm(request.POST)
        if form_ha.is_valid():
            form_ha.save()
            exito = True
    return render(request,'historia_academica.html',{'form':form_ha,'teacher_id':teacher_id,'exito':exito})

def nueva_laboral(request):
    form_ha = HistoriaLaboralForm()
    teacher_id = request.user.id
    exito = False
    if request.method == 'POST':
        form_ha = HistoriaLaboralForm(request.POST)
        if form_ha.is_valid():
            form_ha.save()
            exito = True
    return render(request,'historia_laboral.html',{'form':form_ha,'teacher_id':teacher_id,'exito':exito})
