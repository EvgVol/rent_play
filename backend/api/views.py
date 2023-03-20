from djoser.views import UserViewSet

from .serializers import UsersSerializer
from users.models import User


class CustomUserViewSet(UserViewSet):
    """Вьюсет для кастомной модели пользователя."""
    
    queryset = User.objects.all()
    serializer_class = UsersSerializer
