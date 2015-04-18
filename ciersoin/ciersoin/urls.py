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
    url(r'^teacher/',include('teacher.urls')),
    url(r'^academica-laboral/',include('historiaAcademicaLaboral.urls')),
    url(r'^cursos/',include('cursosCohortesActividades.urls')),
<<<<<<< HEAD
    url(r'^actividades/',include('cursosCohortesActividades.urls')),
    url(r'^cohortes/', include('cursosCohortesActividades.urls')),
=======
    url(r'^reportes/',include('reportes.urls'))
>>>>>>> be3669d3d7979c33a4d1244f03ae61bc098a29f3
)
