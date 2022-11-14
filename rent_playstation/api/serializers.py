from drf_extra_fields.fields import Base64ImageField
from django.conf import settings
from rest_framework import serializers

from user.validators import validate_username
from rent.models import Console, Order
from user.models import User


class SingUpSerializer(serializers.Serializer):
    """Сериализатор для регистрации."""

    email = serializers.EmailField(required=True)
    username = serializers.CharField( 
        required=True,
        validators=(validate_username,)
    )


class GetTokenSerializer(serializers.Serializer):
    """Сериализатор для получения токена при регистрации."""

    username = serializers.CharField( 
        required=True, 
        validators=(validate_username,)
    ) 
    confirmation_code = serializers.CharField(required=True)


class UsersSerializer(serializers.ModelSerializer):
    """Сериализатор для новых юзеров."""

    username = serializers.CharField( 
        required=True, 
        validators=(validate_username,)
    )

    class Meta: 
            abstract = True 
            model = User 
            fields = ('username', 'email', 'first_name',
                      'last_name', 'role') 


class PersSerializer(UsersSerializer): 
    """Сериализатор для пользователя.""" 

    class Meta(UsersSerializer.Meta): 
        read_only_fields = ('role',) 


class ConsoleSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Console
        fields = '__all__'
