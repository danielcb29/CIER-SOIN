__author__ = 'daniel'
from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    url(r'^academica',nueva_academica),
    url(r'^laboral',nueva_laboral),
    url(r'^eliminar/ha/(\d+)',eliminar_ha),
    url(r'^editar/ha/(\d+)',editar_ha),
    url(r'^eliminar/hl/(\d+)',eliminar_hl),
    url(r'^editar/hl/(\d+)',editar_hl),


)
