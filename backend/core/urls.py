from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServiceView.as_view(), name='services'),
    path('contacts/', views.ContactView.as_view(), name='contacts'),

    path('consoles', include('consoles.urls')),
    path('games', include('games.urls')),
    path('blog', include('blog.urls')),
    path('auth', include('users.urls')),
]
