from rest_framework import serializers

from .models import User


class UsersSerializer(serializers.ModelSerializer):
    """Сериализатор для всех пользователей."""

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')
