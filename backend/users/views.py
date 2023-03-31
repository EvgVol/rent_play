from djoser.views import UserViewSet
from django.shortcuts import get_object_or_404
from rest_framework import (filters, permissions, response, status, views,
                            viewsets, decorators)

from .serializers import UsersSerializer
from .models import User


class CustomUserViewSet(UserViewSet):
    """Вьюсет для кастомной модели пользователя."""
    
    queryset = User.objects.all()
    serializer_class = UsersSerializer


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
