from django.db import models, transaction
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