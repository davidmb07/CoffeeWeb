# Generated by Django 5.0.6 on 2024-07-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_alter_usuario_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(blank=True, default='../static/img/profile.jpg', null=True, upload_to='../media'),
        ),
    ]
