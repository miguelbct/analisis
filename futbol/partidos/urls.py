# partidos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('tabla_posiciones/', views.tabla_posiciones, name='tabla_posiciones'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('admin/registrar_equipo/', views.registrar_equipo, name='registrar_equipo'),
    path('admin/registrar_partido/', views.registrar_partido, name='registrar_partido'),
    path('admin/login/', views.admin_login, name='admin_login'),
]
