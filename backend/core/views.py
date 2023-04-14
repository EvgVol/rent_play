from django.shortcuts import render
from rest_framework import permissions, viewsets
from django.http import HttpResponse, Http404

from .models import Period
from .serializers import PeriodSerializers


def index(request):
    template = 'core/index.html'
    return render(request, template)

# def games(request):
#     template = 'games/games.html'
#     return render(request, template)

# def game_id(request):
#     template = 'games/game_id.html'
#     return render(request, template)

# def consoles(request):
#     template = 'consoles/consoles.html'
#     return render(request, template)

# def console_id(request):
#     template = 'consoles/console_id.html'
#     return render(request, template)

# def blog(request):
#     template = 'blog/blog.html'
#     return render(request, template)

# data = {
#     "image": 'basejhhhhhhhhhhhhhh',
#     "name": 'string',
#     "discription": 'string',
#     "etc": 'int',
# }


# def section(request, num):
#     if num == 1:
#         return HttpResponse(data["image"])
#     elif num == 2:
#         return HttpResponse(data["name"])
#     elif num == 3:
#         return HttpResponse(data["discription"])
#     elif num == 4:
#         return HttpResponse(data["etc"])
#     else:
#         raise Http404("NO SUCH CONTENT!")


class PeriodViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения периода аренды."""

    queryset = Period.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = PeriodSerializers
