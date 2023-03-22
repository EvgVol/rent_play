from django.shortcuts import render
from rest_framework import permissions, viewsets, decorators

from .serializers import TimeRentSerializer
from .models import TimeRent


class TimeRentViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения периода аренды."""

    queryset = TimeRent.objects.all()
    serializer_class = TimeRentSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None
