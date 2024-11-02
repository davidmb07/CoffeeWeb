from django.urls import path
from . import views

urlpatterns = [
    path('mis_terrenos/', views.mis_terrenos, name="mis_terrenos"),
    path('crear_terreno/', views.crear_terreno, name='crear_terreno'),
    path('editar_terreno/<int:terreno_id>/', views.editar_terreno, name='editar_terreno'),
    path('eliminar_terreno/<int:terreno_id>/', views.eliminar_terreno, name='eliminar_terreno'),
]