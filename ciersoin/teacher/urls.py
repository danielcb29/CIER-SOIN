__author__ = 'daniel'
from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    url(r'^registrolt$',registro_lt),
)
