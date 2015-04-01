from django.shortcuts import render
from .forms import LeaderTeacherForm,MasterTeacherForm
from .teacherfactory import TeacherFactory
from django.contrib.auth.hashers import make_password,is_password_usable
from .models import LeaderTeacher,Teacher,MasterTeacher
from cursosCohortesActividades.cursoiterator import CursoIterator
from cursosCohortesActividades.models import Aspirante,Curso
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponseRedirect
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
            #Asigancion de aspirante!
            aspirante = Aspirante()
            aspirante.leader_teacher = lt
            aspirante.curso = Curso.objects.get(nombre=request.POST['curso'],area=request.POST['area_interes'])
            aspirante.save()
            #Fin asignacion aspirante!
            lt_form = LeaderTeacherForm()
            exito = True
    return render(request,'index.html',{'form':lt_form,'exito':exito})

def oferta_cursos_lt(request):
    lt_form = LeaderTeacherForm()
    error = ""
    oferta = False
    area = ""
    cursos = []
    disponibilidad_cursos = False
    cc = ""
    if request.method == 'POST':
        cc = request.POST['cc']
        lt = LeaderTeacher.objects.filter(cedula=cc)
        if len(lt) == 0:
            error = 'No se encuentra matriculado aun, debe primero realizar el registro'
        else:
            oferta = True
            lt_obj = lt[0]
            area = lt[0].area_interes
            cursos_iterator = CursoIterator(area,lt_obj)

            if cursos_iterator.len() != 0:
                disponibilidad_cursos = True
                while not cursos_iterator.is_done():
                    cursos.append(cursos_iterator.next())

    return render(request,'index.html',{'form':lt_form,'oferta':oferta,'error':error,'area':area,'cursos':cursos,'disponibilidad':disponibilidad_cursos,'cedula':cc})

def aspirar_curso(request,cc):
    lt = LeaderTeacher.objects.get(cedula=cc)
    curso = Curso.objects.get(nombre=request.POST['cursos-oferta'])
    aspirante = Aspirante()
    aspirante.leader_teacher=lt
    aspirante.curso=curso
    aspirante.save()
    lt_form = LeaderTeacherForm()
    return render(request,'index.html',{'form':lt_form,'exito_app':True})

#Funcionalidades con login
@login_required
@permission_required('teacher.add_masterteacher', login_url="/index")
def crear_mt(request):
    mt_form = MasterTeacherForm()
    exito = False
    if request.method=='POST':
        mt_form = MasterTeacherForm(request.POST)
        if mt_form.is_valid():
            factory = TeacherFactory()
            mt = factory.crearTeacher(mt_form)
            mt.password = make_password(request.POST['password']) #Password seguro encriptado en sha2
            mt.groups.add(3)
            mt.save()
            exito = True
            mt_form = MasterTeacherForm()
    return render(request,'crear_mt.html',{'form':mt_form,'exito':exito})

@login_required
@permission_required('teacher.add_masterteacher', login_url="/index")
def listar_mt(request):
    teachers = MasterTeacher.objects.all()
    return render(request,'listar_mt.html',{'teachers':teachers})

@login_required
@permission_required('teacher.add_masterteacher', login_url="/index")
def eliminar(request,id):
    teach = Teacher.objects.get(id=id)
    if teach.is_active:
        teach.is_active=False
    else:
        teach.is_active=True
    teach.save()
    return HttpResponseRedirect("/teacher/listarmt")
