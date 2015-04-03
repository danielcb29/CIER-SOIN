__author__ = 'daniel'
from cursosCohortesActividades.models import Curso
from areas.models import Area
class CursoObserver():
    area = ""
    nombres_cursos = []

    def update(self,area):
        area_obj = Area.objects.get(nombre=area)
        if self.area != area:
            cursos = Curso.objects.filter(area=area_obj,activo=True)
            self.nombres_cursos = [cur.nombre for cur in cursos]
            self.area = area
        return self.nombres_cursos,area_obj
