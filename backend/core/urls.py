from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServiceView.as_view(), name='services'),
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback'),
    # path('feedback/success/', views.FeedbackSuccessView.as_view(), name='feedback_success'),
    # path('follow/', views.follow_index, name='follow_index'),
    # path('profile/<str:username>/follow/',
    #      views.profile_follow,
    #      name='profile_follow'),
    # path(
    #     'profile/<str:username>/unfollow/',
    #     views.profile_unfollow,
    #     name='profile_unfollow'
    # ),

    path('', include('consoles.urls')),
    path('', include('games.urls')),
    path('', include('blog.urls')),
    path('', include('users.urls')),
]
