from django.shortcuts import get_object_or_404
from rest_framework import serializers

from games.models import Game, Tag, Review, Comment


class GameSerializer(serializers.ModelSerializer):
    """Сериализатор для игр."""

    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'name', 'image', 'description',
                  'slug', 'tags', 'rating')


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
