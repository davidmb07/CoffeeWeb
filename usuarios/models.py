from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Usuario(models.Model):
    id = models.CharField(max_length=15, primary_key=True, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.BigIntegerField()
    descripcion = models.TextField(max_length=500, blank=True, null=True, default='')
    TIPO_USUARIO_CHOICES = [
        ('Caficultor', 'Caficultor'),
        ('UserCooperativa', 'Usuario de Cooperativa'),
        ('AdminCooperativa', 'Administrador de Cooperativa'),
        ('Insumos', 'Proveedor de Insumos'),
        ('AdminCoffeeWeb', 'Administrador de CoffeeWeb'),
    ]
    tipo_usuario = models.CharField(max_length=35, choices=TIPO_USUARIO_CHOICES)
    contrasena = models.CharField(max_length=250)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', default='img/profile.jpg', blank=True, null=True)
    seguidos = models.ManyToManyField('self', related_name='seguidores', symmetrical=False)
    enlace_perfil = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return f'Nombre: {self.nombre} {self.apellido} / Tipo de Usuario: {self.tipo_usuario}'
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_custom_id()
        if self.id and not self.enlace_perfil:
            self.enlace_perfil = self.generate_profile_link()
        super().save(*args, **kwargs)
    
    @staticmethod
    def generate_custom_id():
        today = timezone.now().date()
        date_str = today.strftime('%Y%m%d')

        # Contar los usuarios creados hoy
        count_today = Usuario.objects.filter(id__startswith=date_str).count() + 1

        return f'{date_str}{count_today}'
    
    def generate_profile_link(self):
        return reverse('perfil', kwargs={'enlace_perfil': self.id})

    def delete(self, using=None, keep_parents=False):
        if self.foto_perfil:
            self.foto_perfil.delete()
        self.user.delete()
        super().delete(using, keep_parents)
        
class AdministradorCoffeeWeb(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'AdministradorCoffeeWeb: {self.usuario}'

class AdministradorCooperativa(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'AdministradorCooperativa: {self.usuario}'

class UsuarioCooperativa(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'UsuarioCooperativa: {self.usuario}'

class Caficultor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'Caficultor: {self.usuario}'

class ProveedorInsumos(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'ProveedorInsumos: {self.usuario}'