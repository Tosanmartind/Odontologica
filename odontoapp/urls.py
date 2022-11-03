from .views import index
from django.urls import path , include
from . import views
urlpatterns = [
    path('',index,name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    # Register.
    path('register', views.register, name="register"),
    # Listar Proveedores.
    path('listarProveedores', views.listarProveedores, name="listarProveedores"),
    path('registrarProveedor', views.registrarproveedores, name="registrarProveedor"),
    path('listarclientes', views.listarclientes, name="listarClientes"),
    path('listarempleados', views.listarempleados, name="listarEmpleados"),
    path('registrarempleados', views.registrarempleados, name="registrarEmpleados"),
    path('eliminarProveedor/<int:ID>', views.eliminarProveedor, name="eliminarProveedor"),
    path('eliminarempleado/<int:rut>', views.eliminarEmpleado, name="eliminarempleado"),
    path('eliminarcliente/<str:rut>', views.eliminarCliente, name="eliminarcliente"),
]
