__author__ = 'daniel'
from teacher.models import Teacher
class Sesion():

    def creada(self,user):
        if user.is_authenticated():
            return True
        else:
            return False
