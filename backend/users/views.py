from djoser.views import UserViewSet
from django.shortcuts import get_object_or_404
from rest_framework import (filters, permissions, response, status, views,
                            viewsets, decorators)
from rest_framework.decorators import action

from .serializers import UsersSerializer, PersSerializer
from .permissions import IsAdmin
from .models import User


class CustomUserViewSet(UserViewSet):
    """Вьюсет для кастомной модели пользователя."""
    
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    @action(
        methods=['GET', 'PATCH'],
        detail=False,
        permission_classes=[permissions.IsAuthenticated]
    )
    def me(self, request):
        user = request.user
        if request.method == 'PATCH':
            serializer = PersSerializer(
                user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.Response(
                serializer.data, status=status.HTTP_200_OK
            )
        serializer = PersSerializer(user)
        return response.Response(
            serializer.data, status=status.HTTP_200_OK
        )

    # @decorators.action(
    #     detail=True,
    #     methods=['POST', 'DELETE'],
    #     permission_classes=[IsAdmin]
    # )
    # def moderator(self, request, pk):
    #     user_id = self.kwargs.get('id')
    #     user = get_object_or_404(User, id=user_id)
    #     MODERATOR = 'Модератор'
    #     data = {'role': MODERATOR}
    #     serializer = UsersSerializer(user=user, data=data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return response.Response(serializer.data, status=status.HTTP_200_OK)