from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('registro/', views.registro, name="registro"),
    path('recuperar_cuenta/', views.recuperar_cuenta, name="recuperar_cuenta"),
    path('cambiar_clave/<uidb64>/<token>/', views.cambiar_clave, name='cambiar_clave'),
    path('mi_perfil/', views.mi_perfil, name='mi_perfil'),
    path('perfil/<str:enlace_perfil>/', views.perfil, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('buscar-usuarios/', views.buscar_usuarios, name='buscar_usuarios'),
    path('autocompletar-usuarios/', views.autocompletar_usuarios, name='autocompletar_usuarios'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)