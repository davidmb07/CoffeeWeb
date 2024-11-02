from django.db import models
from usuarios.models import Usuario

# Create your models here.   
class ResultadoEvaluacion(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    altitud = models.FloatField()
    area_cultivada = models.FloatField()
    variedad_cafe = models.CharField(max_length=50)
    edad_cultivo = models.FloatField()
    densidad_plantacion = models.FloatField()
    sistema_cultivo = models.CharField(max_length=50)
    date_ultima_cosecha = models.DateField()
    produccion_anual = models.FloatField()
    tipo_riego = models.CharField(max_length=50)
    fertilizantes = models.CharField(max_length=50)
    cantidad = models.FloatField()
    pesticidas = models.CharField(max_length=50)
    frecuencia = models.FloatField()
    control_plagas = models.CharField(max_length=50)
    sombra = models.CharField(max_length=50)
    porcentaje = models.FloatField()
    plagas = models.CharField(max_length=50)
    enfermedades = models.CharField(max_length=50)
    sintomas_visibles = models.CharField(max_length=50)
    problemas_crecimiento = models.CharField(max_length=50)
    rendimiento_esperado = models.FloatField()
    sugerencias = models.TextField()
    posibles_problemas_futuros = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evaluación de {self.variedad_cafe} por {self.user.nombre}"
