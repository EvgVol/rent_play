from drf_extra_fields.fields import Base64ImageField
from rest_framework import exceptions, serializers, status

from core import texts
from .models import Follow, User


class UsersSerializer(serializers.ModelSerializer):
    """Сериализатор для всех пользователей."""

    avatar = Base64ImageField()
    count_subscriptions = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'avatar', 'birthdate', 'role', 'count_subscriptions')

    def get_count_subscriptions(self, obj):
        """Проверка подписки пользователей."""
        return obj.follower.count()


class FollowSerializer(UsersSerializer):
    """Сериализатор вывода авторов на которых подписан текущий пользователь.
    """

    consoles = serializers.SerializerMethodField(read_only=True)

    class Meta(UsersSerializer.Meta):
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'birthdate', 'role', 'consoles')
        read_only_fields = ('id', 'email', 'username', 'first_name',
                            'last_name', 'birthdate', 'role', 'consoles')

    def validate(self, data):
        author = self.instance
        user = self.context.get('request').user

        if user.is_rentor:
            raise exceptions.ValidationError(
                detail=texts.NO_USER,
                code=status.HTTP_400_BAD_REQUEST
            )
        if not author.is_rentor:
            raise exceptions.ValidationError(
                detail=texts.NO_RENTOR,
                code=status.HTTP_400_BAD_REQUEST
            )
        if Follow.objects.filter(user=user, author=author).exists():
            raise exceptions.ValidationError(
                detail=texts.DUBLICAT_USER,
                code=status.HTTP_400_BAD_REQUEST
            )
        if user == author:
            raise exceptions.ValidationError(
                detail=texts.SELF_FOLLOW,
                code=status.HTTP_400_BAD_REQUEST
            )
        return data

    def get_consoles(self, obj):
        """Достаем приставки."""
        return obj.consoles.all()
