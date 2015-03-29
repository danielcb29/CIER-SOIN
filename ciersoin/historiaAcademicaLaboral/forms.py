__author__ = 'daniel'
from django.forms import ModelForm
from django import forms
from .models import HistoriaLaboral,HistoriaAcademica

class HistoriaAcademicaForm(ModelForm):
    class Meta:
        model = HistoriaAcademica
        fields= ['universidad','titulo','nivel','teacher']
        widgets = {
            'universidad' : forms.TextInput(attrs={'class':'form-control','placeholder':'Universidad...'}),
            'titulo': forms.TextInput(attrs={'class':'form-control','placeholder':'Titulo...'}),
            'nivel': forms.Select(attrs={'class':'form-control chosen-select'}),
            'teacher' : forms.Select(attrs={'class':'combobox'}),
        }

class HistoriaLaboralForm(ModelForm):
    class Meta:
        model = HistoriaLaboral
        fields= ['sede','institucion','grado','tiempo','tipo_ensenanza','anos_exp','teacher']
        widgets = {
            'sede': forms.TextInput(attrs={'class':'form-control','placeholder':'Sede...'}),
            'institucion': forms.TextInput(attrs={'class':'form-control','placeholder':'Universidad...'}),
            'grado': forms.TextInput(attrs={'class':'form-control','placeholder':'Grado...'}),
            'tiempo':forms.TextInput(attrs={'class':'form-control','placeholder':'Anios...','type':'number'}),
            'tipo_ensenanza':forms.TextInput(attrs={'class':'form-control','placeholder':'Tipo ensenanza...'}),
            'anos_exp' : forms.TextInput(attrs={'class':'form-control','placeholder':'Anios experiencia...','type':'number'}),
            'teacher' : forms.Select(attrs={'class':'combobox'}),
        }