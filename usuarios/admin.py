from django.contrib import admin
from .models import Usuario, AdministradorCoffeeWeb, AdministradorCooperativa, UsuarioCooperativa, Caficultor, ProveedorInsumos
from django.contrib.auth.models import User

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'tipo_usuario')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('tipo_usuario',)

    def delete_model(self, obj):
        # Eliminar dependencias manualmente si es necesario
        if obj.tipo_usuario == 'AdminCooperativa':
            AdministradorCooperativa.objects.filter(usuario=obj).delete()
        elif obj.tipo_usuario == 'UserCooperativa':
            UsuarioCooperativa.objects.filter(usuario=obj).delete()
        elif obj.tipo_usuario == 'Caficultor':
            Caficultor.objects.filter(usuario=obj).delete()
        elif obj.tipo_usuario == 'Insumos':
            ProveedorInsumos.objects.filter(usuario=obj).delete()

        # Eliminar el usuario de Django User
        User.objects.filter(pk=obj.user.pk).delete()

        # Llamar al método delete del modelo para eliminar el usuario
        obj.delete()

admin.site.register(Usuario, UsuarioAdmin)

# Registrar el modelo AdministradorCoffeeWeb
@admin.register(AdministradorCoffeeWeb)
class AdministradorCoffeeWebAdmin(admin.ModelAdmin):
    list_display = ('usuario_id', 'nombre', 'apellido', 'email')
    list_select_related = ('usuario',)

    def usuario_id(self, obj):
        return obj.usuario.id

    def nombre(self, obj):
        return obj.usuario.nombre

    def apellido(self, obj):
        return obj.usuario.apellido

    def email(self, obj):
        return obj.usuario.email

@admin.register(AdministradorCooperativa)
class AdministradorCooperativaAdmin(admin.ModelAdmin):
    list_display = ('usuario_id', 'nombre', 'apellido', 'email')
    list_select_related = ('usuario',)

    def usuario_id(self, obj):
        return obj.usuario.id

    def nombre(self, obj):
        return obj.usuario.nombre

    def apellido(self, obj):
        return obj.usuario.apellido

    def email(self, obj):
        return obj.usuario.email

@admin.register(UsuarioCooperativa)
class UsuarioCooperativaAdmin(admin.ModelAdmin):
    list_display = ('usuario_id', 'nombre', 'apellido', 'email')
    list_select_related = ('usuario',)

    def usuario_id(self, obj):
        return obj.usuario.id

    def nombre(self, obj):
        return obj.usuario.nombre

    def apellido(self, obj):
        return obj.usuario.apellido

    def email(self, obj):
        return obj.usuario.email

@admin.register(Caficultor)
class CaficultorAdmin(admin.ModelAdmin):
    list_display = ('usuario_id', 'nombre', 'apellido', 'email')
    list_select_related = ('usuario',)

    def usuario_id(self, obj):
        return obj.usuario.id

    def nombre(self, obj):
        return obj.usuario.nombre

    def apellido(self, obj):
        return obj.usuario.apellido

    def email(self, obj):
        return obj.usuario.email

@admin.register(ProveedorInsumos)
class ProveedorInsumosAdmin(admin.ModelAdmin):
    list_display = ('usuario_id', 'nombre', 'apellido', 'email')
    list_select_related = ('usuario',)

    def usuario_id(self, obj):
        return obj.usuario.id

    def nombre(self, obj):
        return obj.usuario.nombre

    def apellido(self, obj):
        return obj.usuario.apellido

    def email(self, obj):
        return obj.usuario.email