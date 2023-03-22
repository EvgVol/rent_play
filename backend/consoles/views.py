from rest_framework import permissions, viewsets, decorators

from .serializers import ConsoleSerializer, AddShoppingListConsoleSerializer, AddFavoriteConsoleSerializer
from core.utils import add_and_del_console
from .models import Console, Favorite, ShoppingCart


class ConsoleViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения приставок."""

    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None

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
