from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name = "menu"),
    path('recetas/', recetas, name = "recetas"),
    path('clientes/', clientes, name = "clientes"),
    path('empleados/', empleados, name = "empleados"),
    
    
     path('buscar_cliente/', buscarCliente, name="buscar_cliente"),
     path('buscar2/', buscar2, name="buscar2"),
    
]
