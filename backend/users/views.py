from djoser.views import UserViewSet

from api.serializers import UsersSerializer
from .models import User


class CustomUserViewSet(UserViewSet):
    """Вьюсет для кастомной модели пользователя."""
    
    queryset = User.objects.all()
    serializer_class = UsersSerializer