from django.shortcuts import render
from .forms import LeaderTeacherForm
from .teacherfactory import TeacherFactory
from django.contrib.auth.hashers import make_password,is_password_usable
# Create your views here.

def registro_lt(request):
    lt_form = LeaderTeacherForm(request.POST)
    exito = False
    if request.method == 'POST':
        if lt_form.is_valid():
            factory = TeacherFactory()
            lt = factory.crearTeacher(lt_form)
            lt.password = make_password(request.POST['password']) #Password seguro encriptado en sha2
            lt.groups.add(2)
            lt.is_active = False
            lt.save()
            lt_form = LeaderTeacherForm()
            exito = True
    return render(request,'index.html',{'form':lt_form,'exito':exito})

