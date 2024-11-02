# Generated by Django 5.0.6 on 2024-06-27 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_tipo_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministradorAsociacion',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Caficultor',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ProveedorInsumos',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioAsociacion',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usuarios.usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='../perfiles'),
        ),
    ]
