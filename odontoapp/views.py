from django.shortcuts import render, redirect
from django.http import request
from django.contrib.auth import logout
from .forms import UsuarioForm,ProveedorForm,EmpleadoForm
from .models import Proveedor,Cliente,Empleado
# Create your views here.
def index(request):
    return render(request,'pages/index.html')
def logout(request):
    logout(request)
    return redirect('/pages/index.html')
def register(request):
    form = UsuarioForm()

    if request.method== 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    data = {'form':form}
    return render(request,'registration/register.html',data)   

def listarProveedores(request):
    Proveedores = Proveedor.objects.all()

    return render(request,'pages/listarProveedores.html',{'Proveedores':Proveedores})

def registrarproveedores(request):
    form = ProveedorForm()
    if request.method== 'POST':
        form = ProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('listarProveedores')
    data = {'form':form}
    return render(request,'pages/registrarproveedores.html',data)
    

def listarclientes(request):
    Clientes = Cliente.objects.all()
    return render(request,'pages/listarclientes.html',{'Clientes':Clientes})

def listarempleados(request):
    Empleados = Empleado.objects.all()
    return render(request,'pages/listarempleados.html',{'Empleados':Empleados})

def registrarempleados(request):
    form = EmpleadoForm()
    if request.method== 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('listarEmpleados')
    data = {'form':form}
    return render(request,'pages/registrarempleados.html',data)

def eliminarProveedor(request, ID):
    proveedor = Proveedor.objects.get(ID = ID)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('/listarProveedores')
    return render(request, 'pages/eliminarproveedor.html', {'proveedor':proveedor})

def eliminarEmpleado(request, rut):
    empleado = Empleado.objects.get(rut = rut)
    if request.method == 'POST':
        empleado.delete()
        return redirect('/listarempleados')
    return render(request, 'pages/eliminarempleado.html', {'empleado':empleado})

def eliminarCliente(request, rut):
    cliente = Cliente.objects.get(rut = rut)
    if request.method == 'POST':
        cliente.delete()
        return redirect('/listarclientes')
    return render(request, 'pages/eliminarcliente.html', {'cliente':cliente})