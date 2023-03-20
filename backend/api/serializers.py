from rest_framework import serializers

from users.models import User
from consoles.models import Console, Game


class UsersSerializer(serializers.ModelSerializer):
    """Сериализатор для всех пользователей."""

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')


class ConsoleSerializer(serializers.ModelSerializer):
    """Сериализатор для консолей."""

    class Meta:
        model = Console
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    """Сериализатор для игр."""

    class Meta:
        model = Game
        fields = '__all__'
