__author__ = 'daniel'
from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
                       url(r'^ver',consultar_calificaciones),
                       url(r'^calificar$',calificar),
                       url(r'^calificar/(\d+)/(\d+)$',ingresar_notas),

)
