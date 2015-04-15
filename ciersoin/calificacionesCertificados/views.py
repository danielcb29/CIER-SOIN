from django.shortcuts import render
from .estadoCurso import Contexto

# Create your views here.
def consultar_calificaciones(request):
    return render(request,'admin.html',{})

# Metodo para la generacion de certificados
def generar_Certificado(request, idTeacher):
    return 0




