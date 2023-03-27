from rest_framework import permissions, viewsets, decorators

from api.pagination import LimitPageNumberPagination
from .serializers import ConsoleCreateSerializer, ConsoleReadSerializer, AddShoppingListConsoleSerializer, AddFavoriteConsoleSerializer, CategorySerializer
from core.utils import add_and_del_console
from .models import Console, Favorite, ShoppingCart, Category


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

    queryset = Console.objects.all()
    serializer_class = ConsoleReadSerializer
    permission_classes = (permissions.AllowAny,)
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
