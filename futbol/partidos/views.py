# partidos/views.py

from django.shortcuts import render, redirect
from .models import Equipo
from .forms import EquipoForm, PartidoForm
from django.contrib.auth import authenticate, login

def tabla_posiciones(request):
    equipos = Equipo.objects.all()
    tabla = []

    for equipo in equipos:
        tabla.append({
            'nombre': equipo.nombre,
            'puntos': equipo.puntos(),
            'partidos_jugados': equipo.partidos_jugados(),
            'partidos_ganados': equipo.partidos_ganados(),
            'partidos_empatados': equipo.partidos_empatados(),
            'partidos_perdidos': equipo.partidos_perdidos(),
            'goles_a_favor': equipo.goles_a_favor(),
            'goles_en_contra': equipo.goles_en_contra(),
        })

    tabla = sorted(tabla, key=lambda x: (x['puntos'], x['goles_a_favor'] - x['goles_en_contra'], x['goles_a_favor']), reverse=True)

    return render(request, 'partidos/tabla_posiciones.html', {'tabla': tabla})

def registrar_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EquipoForm()
    return render(request, 'partidos/registrar_equipo.html', {'form': form})

def registrar_partido(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PartidoForm()
    return render(request, 'partidos/registrar_partido.html', {'form': form})

def admin_panel(request):
    return render(request, 'partidos/admin_panel.html')
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir al panel de administrador o a cualquier otra página deseada
            return redirect('admin_panel')
        else:
            # Mostrar un mensaje de error o realizar alguna acción adicional si la autenticación falla
            pass
    return render(request, 'partidos/admin_login.html')