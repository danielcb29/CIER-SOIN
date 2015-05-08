from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Curso)
admin.site.register(Cohorte)
admin.site.register(Actividad)
admin.site.register(Actividad_Cohorte)
admin.site.register(Aspirante)