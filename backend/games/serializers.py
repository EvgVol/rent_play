from django.shortcuts import get_object_or_404
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers, validators

from core import texts
from games.models import (Game, Tag, Review, Comment, FavoriteGame,
                          ShoppingList)
from core.likedislike import LikeDislike


class GameSerializer(serializers.ModelSerializer):
    """Сериализатор для игр."""

    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'name', 'image', 'description',
                  'tags', 'rating')


class ShowGameAddedSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Game.
    Определён укороченный набор полей для некоторых эндпоинтов."""

    image = Base64ImageField()

    class Meta:
        model = Game
        fields = ('id', 'name', 'image', 'tags')


class AddFavoriteGameSerializer(serializers.ModelSerializer):
    """Сериализатор добавления игр в избранное."""

    class Meta:
        model = FavoriteGame
        fields = ('user', 'game')
        validators = [
            validators.UniqueTogetherValidator(
                queryset=FavoriteGame.objects.all(),
                fields=['user', 'game'],
                message=texts.CONSOLE_IN_FAVORITE
            )
        ]

    def to_representation(self, instance):
        request = self.context.get('request')
        return ShowGameAddedSerializer(
            instance.game,
            context={'request': request}
        ).data


class AddShoppingListGameSerializer(AddFavoriteGameSerializer):
    """Сериализатор добавления игр в список покупок."""

    class Meta(AddFavoriteGameSerializer.Meta):
        model = ShoppingList
        validators = [
            validators.UniqueTogetherValidator(
                queryset=ShoppingList.objects.all(),
                fields=['user', 'game'],
                message=texts.ALREADY_BUY
            )
        ]

    def to_representation(self, instance):
        request = self.context.get('request')
        return ShowGameAddedSerializer(
            instance.game,
            context={'request': request}
        ).data


class TagSerializer(serializers.ModelSerializer):
    """Сериализатор для игр."""

    class Meta:
        model = Tag
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания отзывов."""

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True, many=False, )
    score = serializers.IntegerField(max_value=10, min_value=1)

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        read_only = ('id',)

    def validate(self, data):
        request = self.context.get('request')

        if request.method == 'POST':
            game_id = self.context['view'].kwargs.get('game_id')
            game = get_object_or_404(Game, pk=game_id)
            if Review.objects.filter(
                    author=request.user, game=game
            ).exists():
                raise serializers.ValidationError(
                    'Вы уже оставили отзыв!')
        return data


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с комментариями."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
        read_only = ('review',)


class LikeConsole(serializers.ModelSerializer):

    class Meta:
        model = LikeDislike
        fields = '__all__'
