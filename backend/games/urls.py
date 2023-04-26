from django.urls import path

from . import views


urlpatterns = [
    path('/', views.GamesView.as_view(), name='games'),
    path('/1/', views.GameDetailView.as_view(), name='game_detail'),
]
