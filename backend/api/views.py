from urllib.parse import unquote

from django.conf import settings
from djoser.views import UserViewSet
from rest_framework import decorators, permissions, response, status, viewsets

from .serializers import UsersSerializer, ConsoleSerializer, GameSerializer
from users.models import User
from consoles.models import Console, Game



class CustomUserViewSet(UserViewSet):
    """Вьюсет для кастомной модели пользователя."""
    
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class ConsoleViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения приставок."""

    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения игр."""

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None

    # def get_queryset(self):
    #     """Получает игру в соответствии с параметрами запроса."""
    #     title = self.request.query_params.get('title')
    #     queryset = self.queryset
    #     if title:
    #         if title[0] == '%':
    #             title = unquote(title)
    #         else:
    #             title = title.translate(settings.INCORRECT_LAYOUT)
    #         title = title.lower()
    #         start_queryset = list(queryset.filter(title__istartswith=title))
    #         game_set = set(start_queryset)
    #         cont_queryset = queryset.filter(title__icontains=title)
    #         start_queryset.extend(
    #             [game for game in cont_queryset if game not in game_set]
    #         )
    #         queryset = start_queryset
    #     return queryset