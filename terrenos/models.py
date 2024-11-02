from django.db import models
from usuarios.models import Caficultor

# Create your models here.
class Terreno(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    tipo_calle = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    numero1 = models.CharField(max_length=10)
    numero2 = models.IntegerField()
    area = models.IntegerField()
    nivelacion = models.CharField(max_length=50, choices=[('Plano', 'Plano'), ('Pendiente', 'Pendiente')])
    tipo_suelo = models.CharField(max_length=50, choices=[('Arcilloso', 'Arcilloso'), ('Arenoso', 'Arenoso'), ('Franco', 'Franco')])
    caficultor = models.ForeignKey(Caficultor, on_delete=models.CASCADE)
    altitud = models.IntegerField()

    def __str__(self):
        return f'Terreno: {self.nombre}'