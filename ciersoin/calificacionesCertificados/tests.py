from django.test import TestCase
from .estadoCurso import EstadoCursoNoExiste
from teacher.models import LeaderTeacher,MasterTeacher
from cursosCohortesActividades.models import Curso,Actividad,Aspirante,Cohorte,Actividad_Cohorte
from areas.models import Area
from .models import Calificacion
import datetime
# Create your tests here.

class CertificadoTest(TestCase):

    def setUp(self):
        i = 0

    def test_posible_certificado_Uno(self):
        """Es posible obtener un certificado"""
        estado_curso = EstadoCursoNoExiste()
        area = Area.objects.create(nombre='area_1',descripcion='descripcion')
        curso = Curso.objects.create(nombre='curso_1',descripcion='descripcion',area=area)
        actividad = Actividad.objects.create(nombre='actividad_1',descripcion='descripcion',curso=curso)
        lt1 = LeaderTeacher.objects.create(username='username_lt_1', email = 'useremaillt1@gmail.com', password = 'userpass_lt_1', first_name='name_lt_1',last_name='last_name_lt_1',cedula = '1234',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        lt2 = LeaderTeacher.objects.create(username='username_lt_2', email = 'useremaillt1@gmail.com', password = 'userpass_lt_2', first_name='name_lt_2',last_name='last_name_lt_2',cedula = '12345',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        asp = Aspirante.objects.create(leader_teacher=lt1,curso=curso)
        asp2 = Aspirante.objects.create(leader_teacher=lt2,curso=curso, asistencia = False)
        mt = MasterTeacher.objects.create(username='username_mt_1', email = 'useremailmt1@gmail.com', password = 'userpass_mt_1',first_name='name_mt_1',last_name='last_name_mt_1',cedula = '4321',direccion = 'dir_mt_1',municipio  = 'municipio_mt_1',area_interes=area)
        coh = Cohorte.objects.create(numero_cohorte= int(11), fecha_inicial = datetime.date(2015,9,19),fecha_final = datetime.date(2015,7,19),curso = curso,master_teacher = mt)
        coh.estudiantes.add(lt1)
        coh.estudiantes.add(lt2)
        act_coh = Actividad_Cohorte.objects.create(actividad = actividad,cohorte = coh ,fecha_inicial = datetime.date(2015,2,19),fecha_entrega = datetime.date(2015,7,19))
        cal = Calificacion.objects.create(valor = 0,actividad_cohorte = act_coh,leader_teacher = lt1)
        self.assertEqual(estado_curso.posible(lt1.id, coh.id), False)
        #self.assertEqual(cat.speak(), 'The cat says "meow"')

    def test_posible_certificado_Dos(self):
        """Es posible obtener un certificado"""
        estado_curso = EstadoCursoNoExiste()
        area = Area.objects.create(nombre='area_1',descripcion='descripcion')
        curso = Curso.objects.create(nombre='curso_1',descripcion='descripcion',area=area)
        actividad = Actividad.objects.create(nombre='actividad_1',descripcion='descripcion',curso=curso)
        lt1 = LeaderTeacher.objects.create(username='username_lt_1', email = 'useremaillt1@gmail.com', password = 'userpass_lt_1', first_name='name_lt_1',last_name='last_name_lt_1',cedula = '1234',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        lt2 = LeaderTeacher.objects.create(username='username_lt_2', email = 'useremaillt1@gmail.com', password = 'userpass_lt_2', first_name='name_lt_2',last_name='last_name_lt_2',cedula = '12345',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        asp = Aspirante.objects.create(leader_teacher=lt1,curso=curso)
        asp2 = Aspirante.objects.create(leader_teacher=lt2,curso=curso, asistencia = False)
        mt = MasterTeacher.objects.create(username='username_mt_1', email = 'useremailmt1@gmail.com', password = 'userpass_mt_1',first_name='name_mt_1',last_name='last_name_mt_1',cedula = '4321',direccion = 'dir_mt_1',municipio  = 'municipio_mt_1',area_interes=area)
        coh = Cohorte.objects.create(numero_cohorte= int(11), fecha_inicial = datetime.date(2015,9,19),fecha_final = datetime.date(2015,7,19),curso = curso,master_teacher = mt)
        coh.estudiantes.add(lt1)
        coh.estudiantes.add(lt2)
        act_coh = Actividad_Cohorte.objects.create(actividad = actividad,cohorte = coh ,fecha_inicial = datetime.date(2015,2,19),fecha_entrega = datetime.date(2015,7,19))
        cal = Calificacion.objects.create(valor = -6,actividad_cohorte = act_coh,leader_teacher = lt1)
        self.assertEqual(estado_curso.posible(lt1.id, coh.id), False)
        #self.assertEqual(cat.speak(), 'The cat says "meow"')

    def test_posible_certificado_Tres(self):
        """Es posible obtener un certificado"""
        estado_curso = EstadoCursoNoExiste()
        area = Area.objects.create(nombre='area_1',descripcion='descripcion')
        curso = Curso.objects.create(nombre='curso_1',descripcion='descripcion',area=area)
        actividad = Actividad.objects.create(nombre='actividad_1',descripcion='descripcion',curso=curso)
        lt1 = LeaderTeacher.objects.create(username='username_lt_1', email = 'useremaillt1@gmail.com', password = 'userpass_lt_1', first_name='name_lt_1',last_name='last_name_lt_1',cedula = '1234',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        lt2 = LeaderTeacher.objects.create(username='username_lt_2', email = 'useremaillt1@gmail.com', password = 'userpass_lt_2', first_name='name_lt_2',last_name='last_name_lt_2',cedula = '12345',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        asp = Aspirante.objects.create(leader_teacher=lt1,curso=curso)
        asp2 = Aspirante.objects.create(leader_teacher=lt2,curso=curso, asistencia = False)
        mt = MasterTeacher.objects.create(username='username_mt_1', email = 'useremailmt1@gmail.com', password = 'userpass_mt_1',first_name='name_mt_1',last_name='last_name_mt_1',cedula = '4321',direccion = 'dir_mt_1',municipio  = 'municipio_mt_1',area_interes=area)
        coh = Cohorte.objects.create(numero_cohorte= int(11), fecha_inicial = datetime.date(2015,9,19),fecha_final = datetime.date(2015,7,19),curso = curso,master_teacher = mt)
        coh.estudiantes.add(lt1)
        coh.estudiantes.add(lt2)
        act_coh = Actividad_Cohorte.objects.create(actividad = actividad,cohorte = coh ,fecha_inicial = datetime.date(2015,2,19),fecha_entrega = datetime.date(2015,7,19))
        cal = Calificacion.objects.create(valor = 5.5,actividad_cohorte = act_coh,leader_teacher = lt1)
        self.assertEqual(estado_curso.posible(lt1.id, coh.id), False)
        #self.assertEqual(cat.speak(), 'The cat says "meow"')

    def test_posible_certificado_Cuatro(self):
        """Es posible obtener un certificado"""
        estado_curso = EstadoCursoNoExiste()
        area = Area.objects.create(nombre='area_1',descripcion='descripcion')
        curso = Curso.objects.create(nombre='curso_1',descripcion='descripcion',area=area)
        actividad = Actividad.objects.create(nombre='actividad_1',descripcion='descripcion',curso=curso)
        lt1 = LeaderTeacher.objects.create(username='username_lt_1', email = 'useremaillt1@gmail.com', password = 'userpass_lt_1', first_name='name_lt_1',last_name='last_name_lt_1',cedula = '1234',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        lt2 = LeaderTeacher.objects.create(username='username_lt_2', email = 'useremaillt1@gmail.com', password = 'userpass_lt_2', first_name='name_lt_2',last_name='last_name_lt_2',cedula = '12345',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        asp = Aspirante.objects.create(leader_teacher=lt1,curso=curso,asistencia = True)
        asp2 = Aspirante.objects.create(leader_teacher=lt2,curso=curso, asistencia = True)
        mt = MasterTeacher.objects.create(username='username_mt_1', email = 'useremailmt1@gmail.com', password = 'userpass_mt_1',first_name='name_mt_1',last_name='last_name_mt_1',cedula = '4321',direccion = 'dir_mt_1',municipio  = 'municipio_mt_1',area_interes=area)
        coh = Cohorte.objects.create(numero_cohorte= int(11), fecha_inicial = datetime.date(2015,9,19),fecha_final = datetime.date(2015,7,19),curso = curso,master_teacher = mt)
        coh.estudiantes.add(lt1)
        coh.estudiantes.add(lt2)
        act_coh = Actividad_Cohorte.objects.create(actividad = actividad,cohorte = coh ,fecha_inicial = datetime.date(2015,2,19),fecha_entrega = datetime.date(2015,7,19))
        cal = Calificacion.objects.create(valor = 2.50001 ,actividad_cohorte = act_coh,leader_teacher = lt1)
        self.assertEqual(estado_curso.posible(lt1.id, coh.id), True)
        #self.assertEqual(cat.speak(), 'The cat says "meow"')

    def test_posible_certificado_Cinco(self):
        """Es posible obtener un certificado"""
        estado_curso = EstadoCursoNoExiste()
        area = Area.objects.create(nombre='area_1',descripcion='descripcion')
        curso = Curso.objects.create(nombre='curso_1',descripcion='descripcion',area=area)
        actividad = Actividad.objects.create(nombre='actividad_1',descripcion='descripcion',curso=curso)
        lt1 = LeaderTeacher.objects.create(username='username_lt_1', email = 'useremaillt1@gmail.com', password = 'userpass_lt_1', first_name='name_lt_1',last_name='last_name_lt_1',cedula = '1234',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        lt2 = LeaderTeacher.objects.create(username='username_lt_2', email = 'useremaillt1@gmail.com', password = 'userpass_lt_2', first_name='name_lt_2',last_name='last_name_lt_2',cedula = '12345',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        asp = Aspirante.objects.create(leader_teacher=lt1,curso=curso, asistencia = True)
        asp2 = Aspirante.objects.create(leader_teacher=lt2,curso=curso, asistencia = True)
        mt = MasterTeacher.objects.create(username='username_mt_1', email = 'useremailmt1@gmail.com', password = 'userpass_mt_1',first_name='name_mt_1',last_name='last_name_mt_1',cedula = '4321',direccion = 'dir_mt_1',municipio  = 'municipio_mt_1',area_interes=area)
        coh = Cohorte.objects.create(numero_cohorte= int(11), fecha_inicial = datetime.date(2015,9,19),fecha_final = datetime.date(2015,7,19),curso = curso,master_teacher = mt)
        coh.estudiantes.add(lt1)
        coh.estudiantes.add(lt2)
        act_coh = Actividad_Cohorte.objects.create(actividad = actividad,cohorte = coh ,fecha_inicial = datetime.date(2015,2,19),fecha_entrega = datetime.date(2015,7,19))
        cal = Calificacion.objects.create(valor = 3,actividad_cohorte = act_coh,leader_teacher = lt1)
        self.assertEqual(estado_curso.posible(lt1.id, coh.id), True)
        #self.assertEqual(cat.speak(), 'The cat says "meow"')

    def test_posible_certificado_Seis(self):
        """Es posible obtener un certificado"""
        estado_curso = EstadoCursoNoExiste()
        area = Area.objects.create(nombre='area_1',descripcion='descripcion')
        curso = Curso.objects.create(nombre='curso_1',descripcion='descripcion',area=area)
        actividad = Actividad.objects.create(nombre='actividad_1',descripcion='descripcion',curso=curso)
        lt1 = LeaderTeacher.objects.create(username='username_lt_1', email = 'useremaillt1@gmail.com', password = 'userpass_lt_1', first_name='name_lt_1',last_name='last_name_lt_1',cedula = '1234',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        lt2 = LeaderTeacher.objects.create(username='username_lt_2', email = 'useremaillt1@gmail.com', password = 'userpass_lt_2', first_name='name_lt_2',last_name='last_name_lt_2',cedula = '12345',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        asp = Aspirante.objects.create(leader_teacher=lt1,curso=curso, asistencia = True)
        asp2 = Aspirante.objects.create(leader_teacher=lt2,curso=curso, asistencia = True)
        mt = MasterTeacher.objects.create(username='username_mt_1', email = 'useremailmt1@gmail.com', password = 'userpass_mt_1',first_name='name_mt_1',last_name='last_name_mt_1',cedula = '4321',direccion = 'dir_mt_1',municipio  = 'municipio_mt_1',area_interes=area)
        coh = Cohorte.objects.create(numero_cohorte= int(11), fecha_inicial = datetime.date(2015,9,19),fecha_final = datetime.date(2015,7,19),curso = curso,master_teacher = mt)
        coh.estudiantes.add(lt1)
        coh.estudiantes.add(lt2)
        act_coh = Actividad_Cohorte.objects.create(actividad = actividad,cohorte = coh ,fecha_inicial = datetime.date(2015,2,19),fecha_entrega = datetime.date(2015,7,19))
        cal = Calificacion.objects.create(valor = 3.50001,actividad_cohorte = act_coh,leader_teacher = lt1)
        self.assertEqual(estado_curso.posible(lt1.id, coh.id), True)
        #self.assertEqual(cat.speak(), 'The cat says "meow"')

    def test_posible_certificado_Siete(self):
        """Es posible obtener un certificado"""
        estado_curso = EstadoCursoNoExiste()
        area = Area.objects.create(nombre='area_1',descripcion='descripcion')
        curso = Curso.objects.create(nombre='curso_1',descripcion='descripcion',area=area)
        actividad = Actividad.objects.create(nombre='actividad_1',descripcion='descripcion',curso=curso)
        lt1 = LeaderTeacher.objects.create(username='username_lt_1', email = 'useremaillt1@gmail.com', password = 'userpass_lt_1', first_name='name_lt_1',last_name='last_name_lt_1',cedula = '1234',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        lt2 = LeaderTeacher.objects.create(username='username_lt_2', email = 'useremaillt1@gmail.com', password = 'userpass_lt_2', first_name='name_lt_2',last_name='last_name_lt_2',cedula = '12345',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        asp = Aspirante.objects.create(leader_teacher=lt1,curso=curso, asistencia = True)
        asp2 = Aspirante.objects.create(leader_teacher=lt2,curso=curso, asistencia = False)
        mt = MasterTeacher.objects.create(username='username_mt_1', email = 'useremailmt1@gmail.com', password = 'userpass_mt_1',first_name='name_mt_1',last_name='last_name_mt_1',cedula = '4321',direccion = 'dir_mt_1',municipio  = 'municipio_mt_1',area_interes=area)
        coh = Cohorte.objects.create(numero_cohorte= int(11), fecha_inicial = datetime.date(2015,9,19),fecha_final = datetime.date(2015,7,19),curso = curso,master_teacher = mt)
        coh.estudiantes.add(lt1)
        coh.estudiantes.add(lt2)
        act_coh = Actividad_Cohorte.objects.create(actividad = actividad,cohorte = coh ,fecha_inicial = datetime.date(2015,2,19),fecha_entrega = datetime.date(2015,7,19))
        cal = Calificacion.objects.create(valor = 0,actividad_cohorte = act_coh,leader_teacher = lt1)
        self.assertEqual(estado_curso.posible(lt1.id, coh.id), False)
        #self.assertEqual(cat.speak(), 'The cat says "meow"')

    def test_posible_certificado_Ocho(self):
        """Es posible obtener un certificado"""
        estado_curso = EstadoCursoNoExiste()
        area = Area.objects.create(nombre='area_1',descripcion='descripcion')
        curso = Curso.objects.create(nombre='curso_1',descripcion='descripcion',area=area)
        actividad = Actividad.objects.create(nombre='actividad_1',descripcion='descripcion',curso=curso)
        lt1 = LeaderTeacher.objects.create(username='username_lt_1', email = 'useremaillt1@gmail.com', password = 'userpass_lt_1', first_name='name_lt_1',last_name='last_name_lt_1',cedula = '1234',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        lt2 = LeaderTeacher.objects.create(username='username_lt_2', email = 'useremaillt1@gmail.com', password = 'userpass_lt_2', first_name='name_lt_2',last_name='last_name_lt_2',cedula = '12345',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        asp = Aspirante.objects.create(leader_teacher=lt1,curso=curso, asistencia = True)
        asp2 = Aspirante.objects.create(leader_teacher=lt2,curso=curso, asistencia = True)
        mt = MasterTeacher.objects.create(username='username_mt_1', email = 'useremailmt1@gmail.com', password = 'userpass_mt_1',first_name='name_mt_1',last_name='last_name_mt_1',cedula = '4321',direccion = 'dir_mt_1',municipio  = 'municipio_mt_1',area_interes=area)
        coh = Cohorte.objects.create(numero_cohorte= int(11), fecha_inicial = datetime.date(2015,9,19),fecha_final = datetime.date(2015,7,19),curso = curso,master_teacher = mt)
        coh.estudiantes.add(lt1)
        coh.estudiantes.add(lt2)
        act_coh = Actividad_Cohorte.objects.create(actividad = actividad,cohorte = coh ,fecha_inicial = datetime.date(2015,2,19),fecha_entrega = datetime.date(2015,7,19))
        cal = Calificacion.objects.create(valor = -4,actividad_cohorte = act_coh,leader_teacher = lt1)
        self.assertEqual(estado_curso.posible(lt1.id, coh.id), False)
        #self.assertEqual(cat.speak(), 'The cat says "meow"')