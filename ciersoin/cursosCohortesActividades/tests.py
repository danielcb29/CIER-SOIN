from django.test import TestCase
from .models import Curso,Actividad,Aspirante,Cohorte,Actividad_Cohorte
from .cursoobserver import CursoObserver
from areas.models import Area
import datetime
# Create your tests here.

class CursoObserverTest(TestCase):

    def setUp(self):

        area_1 = Area.objects.create(nombre='area_1',descripcion='descripcion')
        curso_1 = Curso.objects.create(nombre='curso_1',descripcion='descripcion',area=area_1)
        curso_2 = Curso.objects.create(nombre='curso_2',descripcion='descripcion',area=area_1)
        curso_3 = Curso.objects.create(nombre='curso_3',descripcion='descripcion',area=area_1)

        area_2 = Area.objects.create(nombre='area_2',descripcion='descripcion')
        curso_4 = Curso.objects.create(nombre='curso_4',descripcion='descripcion',area=area_2)
        curso_5 = Curso.objects.create(nombre='curso_5',descripcion='descripcion',area=area_2)


    def test_update_cursos(self):
        """Cursos a cargar"""
        curso_observer = CursoObserver()

        #Prueba 1
        area = Area.objects.get(nombre = 'area_1')
        self.assertEqual(curso_observer.update(area),  (['curso_3', 'curso_2', 'curso_1'], area))
    def test_update_cursos_dos(self):
        curso_observer = CursoObserver()
        #Prueba 2
        area = Area.objects.get(nombre = 'area_2')
        self.assertEqual(curso_observer.update(area),  (['curso_5', 'curso_4'], area))
    def test_update_cursos_tres(self):
        curso_observer = CursoObserver()
        #Prueba 3
        try:
            area = Area.objects.get(nombre = '-------------')
        except Exception:
            self.fail('Area no encontrada')
        self.assertEqual(curso_observer.update(area),  ())



# Create your tests here.
