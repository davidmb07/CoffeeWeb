# Generated by Django 5.0.6 on 2024-07-01 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_usuario_id_alter_usuario_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdministradorAsociacion',
            new_name='AdministradorCooperativa',
        ),
        migrations.RenameModel(
            old_name='UsuarioAsociacion',
            new_name='UsuarioCooperativa',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(choices=[('Caficultor', 'Caficultor'), ('UserCooperativa', 'Usuario de Cooperativa'), ('AdminCooperativa', 'Administrador de Cooperativa'), ('Insumos', 'Proveedor de Insumos')], max_length=35),
        ),
    ]