# partidos/forms.py

from django import forms
from .models import Equipo, Partido

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre']

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ['equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante']
