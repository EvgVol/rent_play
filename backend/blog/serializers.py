from django.db import models, transaction
from rest_framework import serializers
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
    

# class PostCreatedSerializer(serializers.ModelSerializer):
#     """Сериализатор для добавления постов."""

#     image = Base64ImageField(max_length=None, use_url=True)
#     game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())

#     class Meta:
#         model = Post
#         fields = ('id', 'name', 'image', 'description', 'game', 'pub_date')
#         read_only = ('id',)

#     def to_representation(self, instance):
#         return PostReadSerializer(instance).data