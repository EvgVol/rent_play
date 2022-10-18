from rest_framework import (mixins,
                            permissions,
                            viewsets)

from .serializers import (ConsoleSerializer,
                          OrderSerializer)
from rent.models import Console, Order


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    pass


class ConsoleViewSet(viewsets.ModelViewSet):
    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer
    permission_classes = [permissions.IsAdminUser]


class OrderViewSet(CreateListViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
