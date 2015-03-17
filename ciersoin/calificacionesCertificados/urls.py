__author__ = 'daniel'
from django.conf.urls import patterns, include, url
from calificacionesCertificados.views import *
urlpatterns = patterns('',
                       url(r'^ver',consultar_calificaciones),
)
