__author__ = 'daniel'
from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
    url(r'^$',dashboards),
)
