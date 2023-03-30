from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from .models import User


class UsersSerializer(serializers.ModelSerializer):
    """Сериализатор для всех пользователей."""

    avatar = Base64ImageField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'avatar', 'birthdate', 'role',)


class PersSerializer(UsersSerializer):
    """Сериализатор для пользователя."""

    class Meta(UsersSerializer.Meta):
        read_only_fields = ('role',)