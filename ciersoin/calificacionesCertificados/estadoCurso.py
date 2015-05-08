__author__ = 'alvaro'
from .models import Certificado,Calificacion
from teacher.models import LeaderTeacher
from cursosCohortesActividades.models import Cohorte,Actividad_Cohorte

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
        return Certificado.objects.get(leader_teacher= LeaderTeacher.objects.get(id=id_teach), cohorte = Cohorte.objects.get(id=id_cohor))

class EstadoCursoNoExiste():

    def posible(self,id_teach,id_cohor):
        lt = LeaderTeacher.objects.get(id=id_teach)
        cohor = Cohorte.objects.get(id=id_cohor)
        actividades = Actividad_Cohorte.objects.filter(cohorte=cohor)
        definitiva = 0.0
        for act in actividades:
            calificacion = Calificacion.objects.get(actividad_cohorte=act,leader_teacher=lt)
            if float(calificacion.valor) == -1.0:
                return False
            definitiva+=calificacion.valor
        definitiva /= len(actividades)
        if definitiva <= 2.5:
            return False
        elif definitiva >= 2.55 and definitiva <= 3.5 :
            cert = Certificado()
            cert.leader_teacher = lt
            cert.cohorte = cohor
            cert.tipo = cert.PARTICIPO
            cert.save()

        elif definitiva >= 3.55 and definitiva <= 5.0:
            cert = Certificado()
            cert.leader_teacher = lt
            cert.cohorte = cohor
            cert.tipo = cert.EXCELENCIA
            cert.save()
        return True

    def generarCertificado(self,id_teach,id_cohor):
        return Certificado.objects.get(leader_teacher= LeaderTeacher.objects.get(id=id_teach), cohorte = Cohorte.objects.get(id=id_cohor))

