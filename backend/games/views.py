from rest_framework import permissions, viewsets

from .serializers import GameSerializer, TagSerializer
from .models import Game, Tag


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения игр."""

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (permissions.AllowAny,)

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


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения тегов."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.AllowAny,)
    