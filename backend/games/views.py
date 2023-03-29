from urllib.parse import unquote

from django.db.models import Avg
from rest_framework import permissions, viewsets, decorators
from rest_framework.generics import get_object_or_404

from api.pagination import LimitPageNumberPagination
from .filters import GameFilter
from .serializers import (GameSerializer, TagSerializer,
                          ReviewCreateSerializer, CommentSerializer,
                          AddFavoriteGameSerializer,
                          AddShoppingListGameSerializer)
from api.permissions import IsAuthorOrAdminOrReadOnly
from .models import Game, Tag, Review, FavoriteGame, ShoppingList
from core.enum import Regex
from core.utils import add_and_del_game


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения игр."""

    queryset = Game.objects.all().order_by('name').annotate(
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

    @decorators.action(
    detail=True,
    methods=['POST', 'DELETE'],
    permission_classes=[permissions.IsAuthenticated]
    )
    def favorite(self, request, pk):
        """Добавляем/удаляем игру в 'избранное'"""
        return add_and_del_game(
            AddFavoriteGameSerializer, FavoriteGame, request, pk
        )

    @decorators.action(
        detail=True,
        methods=['POST', 'DELETE'],
        permission_classes=[permissions.IsAuthenticated]
    )
    def shopping_cart(self, request, pk):
        """Добавляем/удаляем игру в 'бронь'"""
        return add_and_del_game(
            AddShoppingListGameSerializer, ShoppingList, request, pk
        )


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
