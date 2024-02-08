from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('equipos/', equipos, name="equipos"),
    path('heroes/', heroes, name="heroes"),   
    path('villanos/', villanos, name="villanos"),
    path('logros/', logros, name="logros"),
    #
    path('equipo_form/', equipoForm, name="equipo_form"),
    path('villano_form/', villanoForm, name="villano_form"),

    path('buscar/', buscar, name="buscar"),  
    path('buscarEquipo/', buscarEquipo, name="buscarEquipo"),    
]