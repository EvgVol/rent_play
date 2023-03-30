from rest_framework import permissions, viewsets

from .serializers import (RentCreateSerializers, RentReadSerializers,
                          ) 

from .models import Rent




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
