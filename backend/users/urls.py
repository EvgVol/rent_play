from django.urls import path
from django.contrib.auth.views import (LoginView, LogoutView, 
                                       PasswordResetView, 
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)

from . import views


urlpatterns = [
    path('/signup/', views.SignUp.as_view(), name='signup'),
    path('/login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('/logout/',
         LogoutView.as_view(template_name='users/logged_out.html'),
         name='logout'
    ),
    path('reset_password/',
         PasswordResetView.as_view(
             template_name = "users/reset_password.html"
         ),
         name ='reset_password'),
    path('reset_password_sent/',
         PasswordResetDoneView.as_view(
             template_name = "users/password_reset_sent.html"
         ),
         name ='password_reset_done'),
    path('reset/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(
             template_name = "users/password_reset_form.html"
         ),
         name ='password_reset_confirm'),
    path('reset_password_complete/',
         PasswordResetCompleteView.as_view(
             template_name = "users/password_reset_done.html"
         ),
         name ='password_reset_complete'),

# #     # Асинхронный запрос проверки имени пользователя
#     path('/signup/validate_username/',
#          views.validate_username,
#          name='validate_username')
]
