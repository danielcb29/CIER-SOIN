__author__ = 'daniel'
from django.forms import ModelForm
from django import forms
from .models import LeaderTeacher,MasterTeacher

class LeaderTeacherForm(ModelForm):
    class Meta:
        model = LeaderTeacher
        fields = ['username','first_name','last_name','email','password','cedula','direccion','municipio','departamento','zona','area_interes']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control required','placeholder':'Nombre de usuario...'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control required','placeholder':'Nombres...'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control required','placeholder':'Apellidos...'}),
            'email' : forms.TextInput(attrs={'type':'email','class':'form-control required','placeholder':'Correo Electronico...'}),
            'password' : forms.TextInput(attrs={'id':'password','type':'password','class':'form-control required','placeholder':'Contrasena...'}),
            'cedula': forms.NumberInput(attrs={'type':'number','class':'form-control required','placeholder':'Cedula...'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder required':'Direccion...'}),
            'area_interes' : forms.Select(attrs={'class':'form-control required'}),
            'municipio': forms.TextInput(attrs={'class':'form-control required','placeholder':'Municipio...'}),
            'departamento': forms.TextInput(attrs={'class':'form-control required','placeholder':'Departamento...'}),
            'zona': forms.Select(attrs={'class':'form-control required','placeholder':'Zona...'}),
        }

class MasterTeacherForm(ModelForm):
    class Meta:
        model = MasterTeacher
        fields = ['username','first_name','last_name','email','password','cedula','direccion','municipio','departamento','zona','area_interes']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de usuario...','requieried':''}),
            'first_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres...','requieried':''}),
            'last_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Apellidos...','requieried':''}),
            'email' : forms.TextInput(attrs={'type':'email','class':'form-control','placeholder':'Correo Electronico...','requieried':''}),
            'password' : forms.TextInput(attrs={'id':'password','type':'password','class':'form-control','placeholder':'Contrasena...','requieried':''}),
            'cedula': forms.NumberInput(attrs={'type':'number','class':'form-control','placeholder':'Cedula...','requieried':''}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion...','requieried':''}),
            'area_interes' : forms.Select(attrs={'class':'form-control','requieried':''}),
            'municipio': forms.TextInput(attrs={'class':'form-control','placeholder':'Municipio...','requieried':''}),
            'departamento': forms.TextInput(attrs={'class':'form-control','placeholder':'Departamento...','requieried':''}),
            'zona': forms.Select(attrs={'class':'form-control','placeholder':'Zona...','requieried':''}),
        }

