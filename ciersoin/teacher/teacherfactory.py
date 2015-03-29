__author__ = 'daniel'
from teacher.models import LeaderTeacher,MasterTeacher
class TeacherFactory():

    def crearTeacher(self,form):
        return form.save()

    def getTeacher(self,id,tipo):
        if tipo == 'LT':
            return LeaderTeacher.objects.get(id=id)
        else:
            return MasterTeacher.objects.get(id=id)


