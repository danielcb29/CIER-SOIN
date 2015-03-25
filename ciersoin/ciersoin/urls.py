from django.conf.urls import patterns, include, url
from django.contrib import admin
from ciersoin.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ciersoin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$',login),
    url(r'^$',index),
    url(r'^calificaciones/',include('calificacionesCertificados.urls')),
    url(r'^index/',admin_index),
)
