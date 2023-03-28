from django.shortcuts import render

from consoles.models import Console
from .utils import paginator_page


# Главная страница -------------------------------------------------
def index(request):
    """Описывает работу главной страницы."""
    console_list = Console.objects.select_related('name', 'group').all()
    context = {'page_obj': paginator_page(request, console_list)}
    return render(request, 'posts/index.html', context)
