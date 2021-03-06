__author__ = 'daniel'
from django.forms import ModelForm
from django import forms
from .models import LeaderTeacher,MasterTeacher,Teacher

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
            'cedula': forms.TextInput(attrs={'type':'number','min':'0','class':'form-control required','placeholder':'Cedula...'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder required':'Direccion...'}),
            'area_interes' : forms.Select(attrs={'class':'form-control required'}),
            'municipio': forms.TextInput(attrs={'class':'form-control required','placeholder':'Municipio...'}),
            'departamento': forms.Select(attrs={'class':'form-control required','placeholder':'Departamento...'}),
            'zona': forms.Select(attrs={'class':'form-control required','placeholder':'Zona...'}),
        }

class MasterTeacherForm(ModelForm):
    class Meta:
        model = MasterTeacher
        fields = ['username','first_name','last_name','email','password','cedula','direccion','municipio','departamento','zona','area_interes']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control required','placeholder':'Nombre de usuario...'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control required','placeholder':'Nombres...'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control required','placeholder':'Apellidos...'}),
            'email' : forms.TextInput(attrs={'type':'email','class':'form-control required','placeholder':'Correo Electronico...'}),
            'password' : forms.TextInput(attrs={'id':'password','type':'password','class':'form-control required','placeholder':'Contrasena...'}),
            'cedula': forms.TextInput(attrs={'type':'number','min':'0','class':'form-control required','placeholder':'Cedula...'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder required':'Direccion...'}),
            'area_interes' : forms.Select(attrs={'class':'form-control required'}),
            'municipio': forms.TextInput(attrs={'class':'form-control required','placeholder':'Municipio...'}),
            'departamento': forms.Select(attrs={'class':'form-control required','placeholder':'Departamento...'}),
            'zona': forms.Select(attrs={'class':'form-control required','placeholder':'Zona...'}),
        }

class TeacherEditForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['username','first_name','last_name','email','password','direccion','municipio','departamento','zona']
        widgets ={
            'username' : forms.TextInput(attrs={'class':'form-control required','placeholder':'Nombre de usuario...'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control required','placeholder':'Nombres...'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control required','placeholder':'Apellidos...'}),
            'email' : forms.TextInput(attrs={'type':'email','class':'form-control required','placeholder':'Correo Electronico...'}),
            'password' : forms.TextInput(attrs={'id':'password','type':'password','class':'form-control required','placeholder':'Contrasena...'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder required':'Direccion...'}),
            'municipio': forms.TextInput(attrs={'class':'form-control required','placeholder':'Municipio...'}),
            'departamento': forms.Select(attrs={'class':'form-control required','placeholder':'Departamento...'}),
            'zona': forms.Select(attrs={'class':'form-control required','placeholder':'Zona...'}),


        }