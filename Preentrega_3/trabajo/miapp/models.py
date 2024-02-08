from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    integrantes = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"

class Heroe(models.Model):
    nombre = models.CharField(max_length=50)
    identidadSecreta = models.CharField(max_length=50)
    emailContacto = models.EmailField()

    def __str__(self):
        return f"{self.identidadSecreta}, {self.nombre}"

class Villano(models.Model):
    nombre = models.CharField(max_length=50)
    identidadSecreta = models.CharField(max_length=50)
    emailContacto = models.EmailField()
    poderes = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.identidadSecreta}, {self.nombre}"

class Logro(models.Model):
    proeza = models.CharField(max_length=50)
    fecha = models.DateField()
    salvoMundo = models.BooleanField()

    def __str__(self):
        return f"{self.proeza}"
