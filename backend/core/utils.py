from pathlib import Path
from datetime import datetime as dt

from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.shortcuts import HttpResponse
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

# @receiver(post_delete, sender=Recipe)
# def delete_image(sender, instance, *a, **kw):
#     """Удаляет картинку при удаление рецепта."""
#     image = Path(instance.image.path)
#     if image.exists():
#         image.unlink()


# def out_list_ingredients(self, request, ingredients):
#     """Загружает файл *.txt со списком покупок.
#         Доступно только авторизованным пользователям.
#         """
#     user = self.request.user
#     filename = f'{user.username}_shopping_list.txt'

#     today = dt.today()
#     shopping_list = (
#         f'Список покупок для пользователя: {user.username}\n\n'
#         f'Дата: {today:%Y-%m-%d}\n\n'
#     )
#     shopping_list += '\n'.join([
#         f'- {ingredient["ingredient__name"]} '
#         f'({ingredient["ingredient__measurement_unit"]})'
#         f' - {ingredient["amount"]}'
#         for ingredient in ingredients
#     ])
#     shopping_list += f'\n\nFoodgram ({today:%Y})'

#     response = HttpResponse(
#         shopping_list, content_type='text.txt; charset=utf-8'
#     )
#     response['Content-Disposition'] = f'attachment; filename={filename}'
#     return response
