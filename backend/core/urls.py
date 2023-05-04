from django.urls import path, include

from . import views
from users.views import ProfileView

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServiceView.as_view(), name='services'),
    # path('contacts/', views.ContactView.as_view(), name='contacts'),
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback'),
    # path('feedback/success/', views.FeedbackSuccessView.as_view(), name='feedback_success'),
    path('profile/1/', ProfileView.as_view(), name='profile'),
    # path('follow/', views.follow_index, name='follow_index'),
    # path('profile/<str:username>/follow/',
    #      views.profile_follow,
    #      name='profile_follow'),
    # path(
    #     'profile/<str:username>/unfollow/',
    #     views.profile_unfollow,
    #     name='profile_unfollow'
    # ),

    path('consoles', include('consoles.urls')),
    path('games', include('games.urls')),
    path('blog', include('blog.urls')),
    path('auth', include('users.urls')),
]
