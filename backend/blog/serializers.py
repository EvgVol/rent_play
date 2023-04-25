from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import serializers, relations
from drf_extra_fields.fields import Base64ImageField

from .models import Post, Review, Comment
from games.models import Game
from games.serializers import GameSerializer
from users.serializers import UsersSerializer



class PostReadSerializer(serializers.ModelSerializer):
    """Сериализатор для возврата списка постов."""

    image = Base64ImageField()
    game = GameSerializer(read_only=True)
    author = UsersSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'name', 'image', 'description', 'pub_date',
                  'game', 'author')


class PostCreatedSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления постов."""

    author = UsersSerializer(read_only=True)
    image = Base64ImageField(max_length=None, use_url=True)
    game = relations.PrimaryKeyRelatedField(queryset=Game.objects.all(), many=False)
    
    class Meta:
        model = Post
        fields = ('id', 'author', 'name', 'image', 'description',
                  'game')
        read_only_fields = ('author',)

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return PostReadSerializer(instance, context=context).data

    @transaction.atomic
    def create(self, validated_data):
        author = self.context.get('request').user
        post = Post.objects.create(author=author, **validated_data)
        post.save()
        return post

    def validate(self, data):
        game = self.initial_data.get('game')
        if not game:
            raise serializers.ValidationError('Недостаточно данных')
        return data


class ReviewPostSerializer(serializers.ModelSerializer):
    """Сериализатор для создания отзывов."""

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True, many=False,)

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'pub_date')
        read_only = ('id',)

    def validate(self, data):
        request = self.context.get('request')

        if request.method == 'POST':
            post_id = self.context['view'].kwargs.get('post_id')
            post = get_object_or_404(Post, pk=post_id)
            if Review.objects.filter(
                    author=request.user, post=post
            ).exists():
                raise serializers.ValidationError(
                    'Вы уже оставили отзыв!')
        return data


class CommentPostSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с комментариями."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
        read_only = ('review',)
