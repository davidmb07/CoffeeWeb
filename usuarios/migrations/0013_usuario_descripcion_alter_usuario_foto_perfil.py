# Generated by Django 5.0.6 on 2024-07-04 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_remove_usuario_identificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='descripcion',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(blank=True, default='img/profile.jpg', null=True, upload_to='fotos_perfil/'),
        ),
    ]
