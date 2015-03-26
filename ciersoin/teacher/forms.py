__author__ = 'daniel'
from django.forms import ModelForm
from django import forms
from .models import LeaderTeacher,MasterTeacher,HistoriaAcademica,HistoriaLaboral

class LeaderTeacherForm(ModelForm):
    class Meta:
        model = LeaderTeacher
        fields = ['username','first_name','last_name','email','password','numeroIdentificacion','direccion','municipio','departamento','zona']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de usuario...'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres...'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Apellidos...'}),
            'email' : forms.TextInput(attrs={'type':'email','class':'form-control','placeholder':'Correo Electronico...'}),
            'password' : forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'Contrasena...'}),
            'numeroIdentificacion': forms.NumberInput(attrs={'type':'number','class':'form-control','placeholder':'Cedula...'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion...'}),
            'municipio': forms.TextInput(attrs={'class':'form-control','placeholder':'Municipio...'}),
            'departamento': forms.TextInput(attrs={'class':'form-control','placeholder':'Departamento...'}),
            'zona': forms.TextInput(attrs={'class':'form-control','placeholder':'Zona...'}),
        }

class MasterTeacherForm(ModelForm):
    class Meta:
        model = MasterTeacher
        fields = ['username','first_name','last_name','email','password','numeroIdentificacion','direccion','municipio','departamento','zona']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de usuario...'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres...'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Apellidos...'}),
            'email' : forms.TextInput(attrs={'type':'email','class':'form-control','placeholder':'Correo Electronico...'}),
            'password' : forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'Contrasena...'}),
            'numeroIdentificacion': forms.NumberInput(attrs={'type':'number','class':'form-control','placeholder':'Cedula...'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion...'}),
            'municipio': forms.TextInput(attrs={'class':'form-control','placeholder':'Municipio...'}),
            'departamento': forms.TextInput(attrs={'class':'form-control','placeholder':'Departamento...'}),
            'zona': forms.TextInput(attrs={'class':'form-control','placeholder':'Zona...'}),
        }

class HistoriaAcademicaForm(ModelForm):
    class Meta:
        model = HistoriaAcademica

class HistoriaLaboralForm(ModelForm):
    class Meta:
        model = HistoriaLaboral