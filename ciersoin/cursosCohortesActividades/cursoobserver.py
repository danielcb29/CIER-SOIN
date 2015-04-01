__author__ = 'daniel'
from cursosCohortesActividades.models import Curso
class CursoObserver():
    area = ""
    nombres_cursos = []

    def update(self,area):
        if self.area != area:
            cursos = Curso.objects.filter(area=area,activo=True)
            self.nombres_cursos = [cur.nombre for cur in cursos]
        return self.nombres_cursos
