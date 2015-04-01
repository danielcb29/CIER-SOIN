__author__ = 'daniel'
from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    url(r'^registrolt$',registro_lt),
    url(r'^oferta-cursos-lt$',oferta_cursos_lt),
    url(r'^aspirante/(\d+)$',aspirar_curso),
    url(r'^crearmt$',crear_mt),
    url(r'^listarmt$',listar_mt),
    url(r'^eliminar/(\d+)$',eliminar),
    url(r'^listarlt$',listar_lt),
    url(r'^aceptar/(\d+)$',aceptar_lt),
)
