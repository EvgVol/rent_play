from rest_framework import permissions, viewsets

from api.serializers import ConsoleSerializer
from .models import Console, Favorite, ShoppingCart


class ConsoleViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения приставок."""

    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None
