from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path('auth/', include([
        path('signup/', views.SignUp.as_view(), name='signup'),
        path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
        path('logout/', LogoutView.as_view(next_page='core:index'), name='logout'),
        path('password_reset/', include([
            path('', views.PasswordReset.as_view(),  name='password_reset'),
            path('done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
        ])),
        path('password_change/', include([
            path('', views.PasswordChange.as_view(), name='password_change'),
            path('done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
        ])),
        path('reset/', include([
            path('<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm',),
            path('done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
        ])),
    ])),

    path('profile/', include([
        path('', views.ProfileView.as_view(), name='profile'),
        path('edit/', views.ProfileView.as_view(), name='profile'),
        path('', views.ProfileView.as_view(), name='profile'),
        path('', views.ProfileView.as_view(), name='profile'),
    ]))
]
