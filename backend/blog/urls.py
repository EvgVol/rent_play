from django.urls import path

from . import views


urlpatterns = [
    path('/', views.blog, name='blog'),
    path('/1/', views.post, name='sing_post'),
]
