from django.shortcuts import render

# Create your views here.
def dashboards(request):
    return render(request,'reportes.html',{})

def listados(request):
    return render(request,'listados.html',{})