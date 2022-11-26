from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    rut = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Automovil(models.Model):
    patente = models.CharField(max_length=6, blank=True)
    modelo = models.CharField(max_length=50)
    gravedad = models.CharField(max_length=20)
    estado = models.CharField(max_length=30)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = 'automoviles'
        managed = True
        verbose_name = 'Automóvil'
        verbose_name_plural = 'Automóviles'

    def __str__(self):
        return self.modelo