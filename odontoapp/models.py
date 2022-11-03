from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
# Create your models here.
class Cliente(AbstractBaseUser):
    rut = models.CharField(max_length=10,primary_key=True)
    username = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    password = models.CharField(max_length=20, default='password')
    USERNAME_FIELD = 'username'

class Proveedor(models.Model):
    ID = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    direccion = models.CharField(max_length=200)
    rubro = models.CharField(max_length=50)


class Empleado(models.Model):
    rut = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    password = models.CharField(max_length=20, default='password')