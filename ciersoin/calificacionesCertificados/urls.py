__author__ = 'daniel'
from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
                       url(r'^visualizar',consultar_calificaciones),
                       url(r'^calificar$',calificar),
                       url(r'^calificar/(\d+)/(\d+)$',ingresar_notas),
                       url(r'^certificado/(\d+)/(\d+)$',generar_Certificado),
                       url(r'^listar$',listar_calificaciones)

)
