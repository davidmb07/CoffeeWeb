# Generated by Django 5.0.6 on 2024-07-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrenos', '0002_alter_terreno_tipo_suelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='terreno',
            name='altitud',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
