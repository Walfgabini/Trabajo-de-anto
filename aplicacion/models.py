from django.db import models

# Create your models here.
class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    tiempo_preparacion = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.titulo} - ({self.ingredientes}) - ({self.instrucciones}) - ({self.tiempo_preparacion})"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} - ({self.telefono}) - ({self.email}) - ({self.direccion})"
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()
    
    def __str__(self):
        return f"{self.nombre} - ({self.puesto}) - ({self.salario}) - ({self.fecha_contratacion})"