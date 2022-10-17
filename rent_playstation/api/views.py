from django.shortcuts import get_object_or_404
from rest_framework import (mixins,
                            permissions,
                            viewsets)

from .serializers import (ConsoleSerializer,
                          CostSerializer,
                          RentalRateSerializer,
                          OrderSerializer)
from rent.models import Console, Cost, RentalRate, Order


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    pass


class ConsoleViewSet(viewsets.ModelViewSet):
    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer
    permission_classes = [permissions.IsAdminUser]


class RentalRateViewSet(viewsets.ModelViewSet):
    queryset = RentalRate.objects.all()
    serializer_class = RentalRateSerializer
    permission_classes = [permissions.IsAdminUser]


class CostViewSet(viewsets.ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    permission_classes = [permissions.IsAdminUser]



class OrderViewSet(CreateListViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
