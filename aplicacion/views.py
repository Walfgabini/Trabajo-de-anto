from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")


def recetas(request):
    return render(request, 'aplicacion/recetas.html')

def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request, "aplicacion/clientes.html", contexto)

def empleados(request):
    return render(request, "aplicacion/empleados.html")

def buscarCliente(request):
    return render(request, "aplicacion/buscarCliente.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        cliente = Cliente.objects.filter(nombre__icontains=patron)
        contexto = {'clientes': cliente} 
        return render(request, "aplicacion/clientes.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")