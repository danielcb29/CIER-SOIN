__author__ = 'alvaro'
from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = patterns('',
    url(r'^listar-area/(.+)$',listar_curos_area),
    url(r'^crearcurso$', crear_curso),
    url(r'^listarcursos$', listar_curso),
    url(r'^eliminar/(\d+)$',eliminar_curso),
    url(r'^editar/(\d+)$',editar_curso),
    url(r'^crear$',crear_actividad),
    url(r'^listar$',listar_actividades),
    url(r'^editaractividad/(\d+)$',editar_actividad),
    url(r'^eliminaractividad/(\d+)$',eliminar_actividad),
    url(r'^listarcohorte$',listar_cohorte),
    url(r'^editarcohorte/(\d+)$',editar_cohorte),
    url(r'^eliminarcohorte/(\d+)$',eliminar_cohorte),

    url(r'^crearcohorte$',crear_cohorte_paso_curso),
    url(r'^crearcohorte/(.+)$',crear_cohorte_estudiantes),
    url(r'^actividades/(\d+)',crear_cohorte_actividades),
    url(r'^editarcohorte/actividades/(\d+)$',editar_cohorte_actividad),
)
