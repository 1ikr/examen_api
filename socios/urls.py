from django.urls import path
from . import views

urlpatterns = [
    path('introducir_socio/', views.introducir_socio, name='introducir_socio'),
    path('modificar_contraseña/<str:numero_socio>/', views.modificar_contraseña, name='modificar_contraseña'),
    path('obtener_todos_socios/', views.obtener_todos_socios, name='obtener_todos_socios'),
]
