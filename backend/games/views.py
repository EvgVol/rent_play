from urllib.parse import unquote

from rest_framework import permissions, viewsets

from api.pagination import LimitPageNumberPagination
from .filters import GameFilter
from .serializers import GameSerializer, TagSerializer
from .models import Game, Tag
from core.enum import Regex


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения игр."""

    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = LimitPageNumberPagination
    filterset_class = GameFilter

    def get_queryset(self):
        """Получает игры в соответствии с параметрами запроса."""
        name = self.request.query_params.get('name')
        queryset = self.queryset
        if name:
            if name[0] == '%':
                name = unquote(name)
            else:
                name = name.translate(Regex.INCORRECT_LAYOUT)
            name = name.lower()
            start_queryset = list(queryset.filter(name__istartswith=name))
            game_list = set(start_queryset)
            cont_queryset = queryset.filter(name__icontains=name)
            start_queryset.extend(
                [game for game in cont_queryset if game not in game_list]
            )
            queryset = start_queryset
        return queryset


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения тегов."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None
    