from django.urls import path

from . import views


urlpatterns = [
    path('games/', views.GamesView.as_view(), name='games'),
    path('games/1/', views.GameDetailView.as_view(), name='game_detail'),
]
