from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ciersoin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$',iniciar_sesion),
    url(r'^logout',cerrar_sesion),
    url(r'^$',index),
    url(r'^calificaciones/',include('calificacionesCertificados.urls')),
    url(r'^index/',admin_index),
)
