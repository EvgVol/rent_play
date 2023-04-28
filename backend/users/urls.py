from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path('/signup/', views.SignUp.as_view(), name='signup'), #регистрация
    path('/login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'), #Вход
    path('/logout/',
         LogoutView.as_view(next_page='core:index'),
         name='logout' #Выход
    ),
    path(
        '/password_reset/',
        views.PasswordReset.as_view(), #Сброс пароля
        name='password_reset' #'users/password_reset_form.html'
    ),
    path(
        '/password_reset/done/',
        views.PasswordResetDone.as_view(), #Сброс пароля прошёл успешно
        name='password_reset_done' #'users/password_reset_done.html'
    ),
    
    path(
        '/password_change/',
        views.PasswordChange.as_view(), #Пароль изменён
        name='password_change' #'users/password_change_form.html'
    ),
    path(
        '/password_change/done/',
        views.PasswordChangeDone.as_view(),
        name='password_change_done' #'users/password_change_done.html'
    ),

    
    path(
        '/reset/<uidb64>/<token>/',
        views.PasswordResetConfirm.as_view(), #Новый пароль
        name='password_reset_confirm', #'users/password_reset_confirm.html'
    ),
    path(
        '/reset/done/',
        views.PasswordResetComplete.as_view(),
        name='password_reset_complete' #'users/password_reset_complete.html'
    ),

# #     # Асинхронный запрос проверки имени пользователя
#     path('/signup/validate_username/',
#          views.validate_username,
#          name='validate_username')
]
