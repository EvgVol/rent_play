from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    # path('sections/<int:num>', views.section, name='section'),
    path('consoles/', views.consoles, name='consoles'),
    path('consoles/1/', views.console_id, name='console_id'),
    path('games/', views.games, name='games'),
    path('games/1/', views.game_id, name='game_id'),
    path('blog/', views.blog, name='blog'),
]
