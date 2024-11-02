from django.urls import path
from . import views

urlpatterns = [
    path('cultivos/', views.cultivo, name="cultivo"),
    path('suelos/', views.suelo, name="suelo"),
    path('evaluar_cultivo/', views.evaluar_cultivo, name="evaluar_cultivo"),
    path('resultados/', views.resultados, name="resultados"),
]