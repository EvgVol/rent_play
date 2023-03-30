from rest_framework import permissions, viewsets

from .serializers import (RentCreateSerializers, RentReadSerializers,
                          PeriodSerializers,) 

from .models import Rent, Period


class PeriodViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения периода аренды."""

    queryset = Period.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RentReadSerializers


class RentViewSet(viewsets.ModelViewSet):
    """Вьюсет для отображения заказов.
    Для запросов на чтение используется RentReadSerializer
    Для запросов на изменение используется RentCreateSerializers"""

    queryset = Rent.objects.all()
    permission_classes = (permissions.IsAuthenticated,) 
    serializer_class = RentReadSerializers

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT'):
            return RentCreateSerializers
        return RentReadSerializers
