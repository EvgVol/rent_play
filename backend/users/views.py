from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import (decorators, permissions, response, status)

from .models import Follow, User
from .serializers import FollowSerializer, UsersSerializer


class CustomUserViewSet(UserViewSet):
    """Вьюсет для кастомной модели пользователя."""

    queryset = User.objects.all()
    serializer_class = UsersSerializer

    @decorators.action(
        detail=True,
        methods=['POST', 'DELETE'],
        permission_classes=[permissions.IsAuthenticated]
    )
    def subscribe(self, request, **kwargs):
        """Подписываем / отписываемся на арендодателя.
        Доступно только арендателям.
        """
        user = request.user
        author_id = self.kwargs.get('id')
        author = get_object_or_404(User, id=author_id)
        if request.method == 'POST':
            serializer = FollowSerializer(author,
                                          data=request.data,
                                          context={'request': request})
            serializer.is_valid(raise_exception=True)
            Follow.objects.create(user=user, author=author)
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED)
        get_object_or_404(Follow, user=user, author=author).delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    @decorators.action(
        detail=False,
        methods=['GET'],
        permission_classes=(permissions.IsAuthenticated,)
    )
    def subscriptions(self, request):
        """Возвращает пользователей, на которых подписан текущий пользователь.
        В выдачу добавляются рецепты.
        """
        return self.get_paginated_response(
            FollowSerializer(
                self.paginate_queryset(
                    User.objects.filter(following__user=request.user)
                ),
                many=True,
                context={'request': request},
            ).data
        )

    # @decorators.action(
    #     detail=False,
    #     methods=['GET', 'PATCH',],
    #     permission_classes=[permissions.IsAuthenticated]
    # )
    # def me(self, request):
    #     user = request.user

    #     if request.method == 'GET':
    #         serializer = UsersSerializer(user)
    #         return UsersSerializer(user)

    #     if request.method == 'PATCH':
    #         serializer = PersSerializer(
    #             user, data=request.data, partial=True
    #         )
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return response.Response(
    #             serializer.data, status=status.HTTP_200_OK
    #         )
    #     serializer = PersSerializer(user)
    #     return response.Response(
    #         serializer.data, status=status.HTTP_200_OK
        # )
