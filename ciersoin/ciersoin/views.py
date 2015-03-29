__author__ = 'daniel'
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from teacher.forms import LeaderTeacherForm


def iniciar_sesion(request):
    if request.method =='POST':
        usuario = request.POST.get('username')
        contrasena = request.POST.get('password')

        usuario = authenticate(username=usuario,password=contrasena)

        if usuario is not None:
            if usuario.is_active:
                login(request, usuario)
                return HttpResponseRedirect('/index')
            else:
                return render(request,'login.html',{'error':'Su cuenta se encuentra desactivada'})
        else:
            error = "Su nombre de usuario o contrasena son invalidos"
            return render(request,'login.html',{'error':error})
    else:
        return render(request,'login.html',{'error':''})
    return render(request,'login.html',{})

@login_required
def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect('/login')

def index(request):
    lt_form = LeaderTeacherForm()
    return render(request,'index.html',{'form':lt_form,'exito':False})

@login_required(login_url='/login')
def admin_index(request):
    return render(request,'index_admin.html',{})