from django.test import TestCase
from .estadoCurso import EstadoCursoNoExiste
from teacher.models import LeaderTeacher,MasterTeacher
from cursosCohortesActividades.models import Curso,Actividad,Aspirante,Cohorte,Actividad_Cohorte
from areas.models import Area
from .models import Calificacion
import datetime
# Create your tests here.
class CertficadoTest(TestCase):
    def setUp(self):
        '''area = Area.objects.create(nombre='area_1',descripcion='descripcion')
        curso = Curso.objects.create(nombre='curso_1',descripcion='descripcion',area=area)
        actividad = Actividad.objects.create(nombre='actividad_1',descripcion='descripcion',curso=curso)
        lt = LeaderTeacher.objects.create(first_name='name_lt_1',last_name='last_name_lt_1',cedula = '1234',direccion = 'dir_lt_1',municipio  = 'municipio_lt_1',area_interes=area)
        asp = Aspirante.objects.create(leader_teacher=lt,curso=curso)
        mt = MasterTeacher.objects.create(first_name='name_mt_1',last_name='last_name_mt_1',cedula = '4321',direccion = 'dir_mt_1',municipio  = 'municipio_mt_1',area_interes=area)
        coh = Cohorte.objects.create(numero_cohorte = 1,fecha_inicial = datetime.date(2015/2/19),fecha_final = datetime.date(2015/7/19),curso = curso,master_teacher = mt, estudiantes = [lt])
        act_coh = Actividad_Cohorte.objects.create(actividad = actividad,cohorte = coh ,fecha_inicial = datetime.date(2015/2/19),fecha_final = datetime.date(2015/7/19))
        cal = Calificacion.objects.create(valor = 0.0,actividad_cohorte = act_coh,leader_teacher = lt)'''

    def test_posible_certificado(self):
        """Es posible obtener un certificado"""
        estado_curso = EstadoCursoNoExiste()
        #lt = LeaderTeacher.objets.get(fist_name='name_lt_1')
        #ch = Cohorte.objects.get(numero_cohorte=1)
        self.assertEqual(estado_curso.testing_method(5.0,False), (False,'PERDIO'))
        #self.assertEqual(cat.speak(), 'The cat says "meow"')