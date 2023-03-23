from django.db import models, transaction
from rest_framework import serializers

from users.serializers import UsersSerializer
from games.models import Game
from .models import GameInRent, Rent


class GameInRentSerializers(serializers.ModelSerializer):
    """ Сериализатор для вывода игр в заказе. """

    id = serializers.PrimaryKeyRelatedField(
        read_only=True,
        source='game'
    )

    name = serializers.SlugRelatedField(
        source='game',
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = GameInRent
        fields = '__all__'


class GameInRentWriteSerializer(serializers.ModelSerializer):
    """ Сериализатор для игры в заказе."""

    id = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())

    class Meta:
        model = GameInRent
        fields = ('id')


class RentReadSerializers(serializers.ModelSerializer):
    """Сериализатор для возврата списка заказов."""

    user = UsersSerializer(read_only=True)
    games = GameInRentSerializers(many=True,
                                  required=True,
                                  source='game_list')

    class Meta:
        model = Rent
        fields = ('id', 'user', 'games', 'console', 'time',)

    def get_games(self, rent):
        """Получает список игр для заказа."""
        return rent.games.values(
            'id',
            'name'
        )

class RentCreateSerializers(serializers.ModelSerializer):
    """Сериализатор для создание заказов."""

    user = UsersSerializer(read_only=True)
    games = GameInRentWriteSerializer(many=True)

    class Meta:
        model = Rent
        fields = ('id', 'user', 'games', 'console', 'time')
        read_only_fields = ('user',)
    
    @transaction.atomic
    def create_bulk_games(self, games, rent):
        for game in games:
            GameInRent.objects.get_or_create(
                rent=rent,
                game=game['id']
            )

    @transaction.atomic
    def create(self, validated_data):
        game_list = validated_data.pop('games')
        user = self.context.get('request').user
        rent = Rent.objects.create(user=user, **validated_data)
        rent.save()
        self.create_bulk_games(game_list, rent)
        return rent

    @transaction.atomic
    def update(self, instance, validated_data):
        games = validated_data.pop('games')
        instance.games.clear()
        self.create_bulk_games(rent=instance, games=games)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return RentReadSerializers(instance, context=context).data
