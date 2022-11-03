from django import forms
from .models import Cliente,Proveedor,Empleado
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = ['rut','username','nombre','apellido','telefono','direccion']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['ID','nombre','telefono','direccion','rubro']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['rut','nombre','apellido','telefono','direccion']