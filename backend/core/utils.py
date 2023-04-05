from django.core.paginator import Paginator
from rest_framework import response, status
from rest_framework.generics import get_object_or_404

from consoles.models import Console
from games.models import Game

def add_and_del_console(add_serializer, model, request, console_id):
    """Опция добавления и удаления консоли."""
    user = request.user
    data = {'user': user.id,
            'console': console_id}
    serializer = add_serializer(data=data, context={'request': request})
    if request.method == 'POST':
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data,
                                 status=status.HTTP_201_CREATED)
    get_object_or_404(
        model, user=user, console=get_object_or_404(Console, id=console_id)
    ).delete()
    return response.Response(status=status.HTTP_204_NO_CONTENT)


def add_and_del_game(add_serializer, model, request, game_id):
    """Опция добавления и удаления игры."""
    user = request.user
    data = {'user': user.id,
            'game': game_id}
    serializer = add_serializer(data=data, context={'request': request})
    if request.method == 'POST':
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data,
                                 status=status.HTTP_201_CREATED)
    get_object_or_404(
        model, user=user, game=get_object_or_404(Game, id=game_id)
    ).delete()
    return response.Response(status=status.HTTP_204_NO_CONTENT)


def paginator_page(request, queryset):
    """Описывает работу пагинатора."""
    paginator = Paginator(queryset, 8)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
