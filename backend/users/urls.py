from django.urls import path

from . import views


urlpatterns = [
    path('/signup/', views.SignUp.as_view(), name='signup'),
    # Асинхронный запрос проверки имени пользователя
    path('/signup/validate_username/', views.validate_username, name='validate_username')
]
