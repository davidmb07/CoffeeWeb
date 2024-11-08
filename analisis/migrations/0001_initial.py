# Generated by Django 5.0.6 on 2024-07-22 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0018_remove_usuario_slug_usuario_enlace_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultadoEvaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altitud', models.FloatField()),
                ('area_cultivada', models.FloatField()),
                ('variedad_cafe', models.CharField(max_length=50)),
                ('edad_cultivo', models.FloatField()),
                ('densidad_plantacion', models.FloatField()),
                ('sistema_cultivo', models.CharField(max_length=50)),
                ('date_ultima_cosecha', models.DateField()),
                ('produccion_anual', models.FloatField()),
                ('tipo_riego', models.CharField(max_length=50)),
                ('fertilizantes', models.CharField(max_length=50)),
                ('cantidad', models.FloatField()),
                ('pesticidas', models.CharField(max_length=50)),
                ('frecuencia', models.FloatField()),
                ('control_plagas', models.CharField(max_length=50)),
                ('sombra', models.CharField(max_length=50)),
                ('porcentaje', models.FloatField()),
                ('plagas', models.CharField(max_length=50)),
                ('enfermedades', models.CharField(max_length=50)),
                ('sintomas_visibles', models.CharField(max_length=50)),
                ('problemas_crecimiento', models.CharField(max_length=50)),
                ('rendimiento_esperado', models.FloatField()),
                ('sugerencias', models.TextField()),
                ('posibles_problemas_futuros', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
    ]
