from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from users.models import User


class UsersSerializer(serializers.ModelSerializer):
    """Сериализатор для всех пользователей."""

    avatar = Base64ImageField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'role', 'is_active', 'avatar',)
