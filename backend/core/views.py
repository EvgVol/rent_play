from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import Period
from .serializers import PeriodSerializers



def index(request):
    template = 'core/index.html'
    return render(request, template) 

class PeriodViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения периода аренды."""

    queryset = Period.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = PeriodSerializers
