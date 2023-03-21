from rest_framework import serializers

from .models import Game, Tag


class GameSerializer(serializers.ModelSerializer):
    """Сериализатор для игр."""

    class Meta:
        model = Game
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """Сериализатор для игр."""

    class Meta:
        model = Tag
        fields = '__all__'
