from urllib.parse import unquote

from django.db.models import Avg
from rest_framework import permissions, viewsets
from rest_framework.generics import get_object_or_404

from api.pagination import LimitPageNumberPagination
from .filters import GameFilter
from .serializers import (GameSerializer, TagSerializer,
                          ReviewCreateSerializer, CommentSerializer)
from .permissions import IsAuthorOrAdminOrReadOnly
from .models import Game, Tag, Review
from core.enum import Regex


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения игр."""

    queryset = Game.objects.all().annotate(
        rating=Avg('reviews__score')
    )
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


class ReviewViewSet(viewsets.ModelViewSet):
    """Отображение действий с отзывами."""

    serializer_class = ReviewCreateSerializer
    permission_classes = (IsAuthorOrAdminOrReadOnly,)

    def get_game(self):
        return get_object_or_404(
            Game,
            id=self.kwargs.get('game_id')
        )

    def get_queryset(self):
        return self.get_game().reviews.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, game=self.get_game()
        )


class CommentViewSet(viewsets.ModelViewSet):
    """Отображение действий с комментариями."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrAdminOrReadOnly,)

    def get_review(self):
        return get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'),
        )

    def get_queryset(self):
        return self.get_review().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, review=self.get_review()
        )
