from django.shortcuts import render
from .models import Torneio, Atleta


def lista_torneios(request):
    torneios = Torneio.objects.prefetch_related('provas', 'atletas')
    return render(request, 'lista_torneios.html', {'torneios': torneios})


def lista_atletas(request):
    atletas = Atleta.objects.prefetch_related('torneios')
    return render(request, 'lista_atletas.html', {'atletas': atletas})
