from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    fecha = models.DateTimeField()
    capacidad = models.IntegerField()
    
class Porta(models.Model):
    nombre_proyecto = models.CharField(max_length=100)
    descripcion = models.TextField()
    image = models.ImageField(default='static/img')
    link = models.URLField(blank=True, null=True)

class Testimonio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100, default='Puesto Desconocido')
    empresa = models.CharField(max_length=100, default='Empresa Desconocida')


    def __str__(self):
        return self.nombre
    
    