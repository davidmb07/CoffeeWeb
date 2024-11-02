# Generated by Django 5.0.6 on 2024-07-01 22:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_rename_administradorasociacion_administradorcooperativa_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministradorCoffeeWeb',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usuarios.usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(choices=[('Caficultor', 'Caficultor'), ('UserCooperativa', 'Usuario de Cooperativa'), ('AdminCooperativa', 'Administrador de Cooperativa'), ('Insumos', 'Proveedor de Insumos'), ('AdminCoffeeWeb', 'Administrador de CoffeeWeb')], max_length=35),
        ),
    ]