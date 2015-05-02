__author__ = 'alvaro'
from .models import Certificado
from teacher.models import LeaderTeacher
from cursosCohortesActividades.models import Cohorte

class Contexto():

    def existe_certficiado(self,id_teach,id_cohor):
        lt = LeaderTeacher.objects.get(id=id_teach)
        coh = Cohorte.objects.get(id=id_cohor)
        cert = Certificado.objects.filter(leader_teacher=lt,cohorte=coh)
        if len(cert) == 0:
            return False
        else:
            return True

class EstadoCursoExiste():

    def generarCertificado(self,id_teach,id_cohor):
        return Certificado.objects.get(leader_teacher= LeaderTeacher.objects.get(id_teach), cohorte = Cohorte.objects.get(id_cohor))

class EstadoCursoNoExiste():

    def posible(self,id_teach,id_cohor):
        pass

    def generarCertificado(self,id_teach,id_cohor):
        return Certificado.objects.get(leader_teacher= LeaderTeacher.objects.get(id_teach), cohorte = Cohorte.objects.get(id_cohor))

