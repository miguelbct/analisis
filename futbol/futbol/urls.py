# futbol/urls.py

from django.contrib import admin
from django.urls import path, include
from partidos import views

urlpatterns = [
    path('', views.tabla_posiciones, name='home'),
    path('admin/', admin.site.urls),
    path('partidos/', include('partidos.urls')),
]
