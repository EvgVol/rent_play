from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('consoles/', views.consoles, name='consoles'),
    path('games/', views.games, name='games'),
    path('games/1/', views.game_id, name='game_id'),
]
