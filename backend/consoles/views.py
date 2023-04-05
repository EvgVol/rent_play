from django.db.models import Avg
from rest_framework import decorators, permissions, viewsets
from rest_framework.generics import get_object_or_404

from api.pagination import LimitPageNumberPagination
from api.permissions import (IsAuthorOrAdminOrReadOnly,
                             IsRentorOrAdminOrReadOnly)
from core.utils import add_and_del_console
from .models import Category, Console, Favorite, ShoppingCart
from .serializers import (AddFavoriteConsoleSerializer,
                          AddShoppingListConsoleSerializer, CategorySerializer,
                          ConsoleCreateSerializer, ConsoleReadSerializer,
                          ReviewPostSerializer)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения тегов."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None


class ConsoleViewSet(viewsets.ModelViewSet):
    """Вьюсет для отображения приставок.
    Для запросов на чтение используется ConsoleReadSerializer
    Для запросов на изменение используется ConsoleCreateSerializer
    """

    queryset = Console.objects.all().order_by('name').annotate(
        rating=Avg('reviews_console__score')
    )
    serializer_class = ConsoleReadSerializer
    permission_classes = (IsRentorOrAdminOrReadOnly,)
    pagination_class = LimitPageNumberPagination

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT', 'PATCH'):
            return ConsoleCreateSerializer
        return ConsoleReadSerializer

    @decorators.action(
        detail=True,
        methods=['POST', 'DELETE'],
        permission_classes=[permissions.IsAuthenticated]
    )
    def favorite(self, request, pk):
        """Добавляем/удаляем консоль в 'избранное'"""
        return add_and_del_console(
            AddFavoriteConsoleSerializer, Favorite, request, pk
        )

    @decorators.action(
        detail=True,
        methods=['POST', 'DELETE'],
        permission_classes=[permissions.IsAuthenticated]
    )
    def shopping_cart(self, request, pk):
        """Добавляем/удаляем консоль в 'список покупок'"""
        return add_and_del_console(
            AddShoppingListConsoleSerializer, ShoppingCart, request, pk
        )


class ReviewConsoleViewSet(viewsets.ModelViewSet):
    """Отображение действий с отзывами."""

    serializer_class = ReviewPostSerializer
    permission_classes = (IsAuthorOrAdminOrReadOnly,)

    def get_console(self):
        return get_object_or_404(Console, id=self.kwargs.get('console_id'))

    def get_queryset(self):
        return self.get_console().reviews_console.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, console=self.get_console()
        )
