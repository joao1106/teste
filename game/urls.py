from django.urls import path
from . import views  # Importa as views da aplicação game

urlpatterns = [
    path('', views.menu, name='menu'),  # Página inicial do jogo
    path('game/', views.game, name='game'),  # Página inicial do jogo
]
