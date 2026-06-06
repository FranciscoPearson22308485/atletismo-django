from django.urls import path
from . import views

urlpatterns = [
    path('torneios/', views.lista_torneios, name='lista_torneios'),
    path('atletas/', views.lista_atletas, name='lista_atletas'),
]
