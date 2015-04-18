__author__ = 'alvaro'
from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = patterns('',
    url(r'^listar-area/(.+)$',listar_curos_area),
    url(r'^crearcurso$', crear_curso),
    url(r'^listarcursos$', listar_curso),
    url(r'^eliminar/(\d+)$',eliminar_curso),
    url(r'^editar/(\d+)$',editar_curso),
)
