from django.forms import ModelForm
from django import forms
from .models import Curso, Cohorte, Actividad

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'area','semanas']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control required','placeholder':'Nombre...'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control required','placeholder':'Descripcion...'}),
            'area': forms.Select(attrs={'class':'form-control required'}),
            'semanas' : forms.Select(attrs={'class':'form-control required'}),
        }

class ActividadForm(ModelForm):
    class Meta:
        model = Actividad
        fields= ['nombre', 'descripcion','tipo', 'curso']#, 'fecha_entrega']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control required','placeholder':'Nombre...'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control required','placeholder':'Descripcion...'}),
            'tipo': forms.Select(attrs={'class':'form-control required','placeholder':'Tipo...'}),
            'curso': forms.Select(attrs={'class':'form-control required'}),
            #'fecha_entrega': forms.DateTimeInput(attrs={'class':'form-control required', 'placeholder': 'Fecha de entrega....'})
        }

class CohorteForm(ModelForm):
    class Meta:
        model = Cohorte
        fields = ['numero_cohorte', 'fecha_inicial', 'fecha_final', 'periodo', 'estudiantes', 'master_teacher', 'curso']#, 'actividad']
        widgets = {
            'numero_cohorte': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Numero de la cohorte...'}),
            'fecha_inicial': forms.DateInput(attrs={'class':'form-control required','placeholder':'Fecha...'}),
            'fecha_final': forms.DateInput(attrs={'class':'form-control required','placeholder':'Fecha...'}),
            'periodo': forms.Select(attrs={'class':'form-control required','placeholder':'Periodo...'}),
            'estudiantes': forms.SelectMultiple(attrs={'class':'form-control required','placeholder':'Estudiantes...'}),
            'master_teacher': forms.Select(attrs={'class':'form-control required','placeholder':'Master Teacher...'}),
            'curso': forms.Select(attrs={'class':'form-control required'}),
            #'actividad': forms.SelectMultiple(attrs={'class':'form-control required','placeholder':'Actividad...'}),

        }
