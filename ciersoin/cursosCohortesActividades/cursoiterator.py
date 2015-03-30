__author__ = 'daniel'
from cursosCohortesActividades.models import Cohorte,Curso
class CursoIterator():
    index = 0
    cursos_ofertados = []

    def __init__(self,area,teacher):
        cursados = [x.curso.id for x in Cohorte.objects.filter(estudiantes=teacher)]
        self.cursos_ofertados = [y for y in Curso.objects.filter(area=area).exclude(id__in=cursados)]
    def len(self):
        return len(self.cursos_ofertados)
    def next(self):
        curso = self.cursos_ofertados[self.index]
        self.index += 1
        return curso
    def is_done(self):
        if self.index >= len(self.cursos_ofertados):
            return True
        else:
            return False
    def current(self):
        return self.cursos_ofertados[self.index]
    def first(self):
        return self.cursos_ofertados[0]