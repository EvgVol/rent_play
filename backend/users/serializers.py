from rest_framework import serializers, exceptions, status
from drf_extra_fields.fields import Base64ImageField

from .models import User, Follow
from core import texts

class UsersSerializer(serializers.ModelSerializer):
    """Сериализатор для всех пользователей."""

    avatar = Base64ImageField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'avatar', 'birthdate', 'role',)


class FollowSerializer(UsersSerializer):
    """Сериализатор вывода авторов на которых подписан текущий пользователь.
    """

    consoles = serializers.SerializerMethodField(read_only=True)

    class Meta(UsersSerializer.Meta):
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'birthdate', 'role', 'consoles')
        read_only_fields = ('id', 'email', 'username', 'first_name', 'last_name',
                            'birthdate', 'role', 'consoles')

    def validate(self, data):
        author = self.instance
        user = self.context.get('request').user
        if not author.is_rentor:
            raise exceptions.ValidationError(
                detail=texts.NO_RENTOR,
                code=status.HTTP_400_BAD_REQUEST
            )
        elif Follow.objects.filter(user=user, author=author).exists():
            raise exceptions.ValidationError(
                detail=texts.DUBLICAT_USER,
                code=status.HTTP_400_BAD_REQUEST
            )
        elif user == author:
            raise exceptions.ValidationError(
                detail=texts.SELF_FOLLOW,
                code=status.HTTP_400_BAD_REQUEST
            )
        return data

    def get_consoles(self, obj):
        """Достаем приставки."""
        return obj.consoles.all()
