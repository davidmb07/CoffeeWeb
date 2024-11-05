from django.db import models
from usuarios.models import Usuario
from django.utils import timezone

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
    
class ResultadoSuelo(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    altitud = models.FloatField()
    color = models.CharField(max_length=50)
    textura = models.CharField(max_length=50)
    humedad = models.FloatField()
    ph = models.FloatField()
    materia_organica = models.FloatField()
    drenaje = models.CharField(max_length=50)
    compactacion = models.CharField(max_length=50)
    temperatura = models.FloatField()
    nitrogeno = models.FloatField()
    fosforo = models.FloatField()
    potasio = models.FloatField()
    calcio = models.FloatField()
    magnesio = models.FloatField()
    azufre = models.FloatField()
    hierro = models.FloatField()
    manganeso = models.FloatField()
    zinc = models.FloatField()
    cobre = models.FloatField()
    boro = models.FloatField()
    molibdeno = models.FloatField()
    salinidad = models.FloatField()
    fertilizantes = models.CharField(max_length=50)
    cantidades_aplicadas = models.FloatField()
    frecuencia_aplicacion = models.FloatField()

    calidad_suelo = models.FloatField()
    recomendaciones = models.TextField()
    posibles_riesgos = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Análisis de suelo de {self.user} - {self.fecha.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = 'Resultado de Suelo'
        verbose_name_plural = 'Resultados de Suelo'
        ordering = ['-fecha']