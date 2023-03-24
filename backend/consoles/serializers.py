from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers, validators, fields

from core import texts
from .models import Console, Favorite, ShoppingCart


class ConsoleSerializer(serializers.ModelSerializer):
    """Сериализатор для консолей."""

    class Meta:
        model = Console
        fields = '__all__'


class ShowConsoleAddedSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Console.
    Определён укороченный набор полей для некоторых эндпоинтов."""

    image = Base64ImageField()
    is_rent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Console
        fields = ('id', 'name', 'image', 'barcode', 'status')

    def get_status(self,  console):
        """Проверяем статус приставки."""
        request = self.context.get('request')
        return (request and request.user.is_authenticated
                and request.user.rent_item)

class AddFavoriteConsoleSerializer(serializers.ModelSerializer):
    """Сериализатор добавления приставок в избранное."""

    class Meta:
        model = Favorite
        fields = ('user', 'console')
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Favorite.objects.all(),
                fields=['user', 'console'],
                message=texts.CONSOLE_IN_FAVORITE
            )
        ]

    def to_representation(self, instance):
        request = self.context.get('request')
        return ShowConsoleAddedSerializer(
            instance.console,
            context={'request': request}
        ).data


class AddShoppingListConsoleSerializer(AddFavoriteConsoleSerializer):
    """Сериализатор добавления приставок в список покупок."""

    class Meta(AddFavoriteConsoleSerializer.Meta):
        model = ShoppingCart
        validators = [
            validators.UniqueTogetherValidator(
                queryset=ShoppingCart.objects.all(),
                fields=['user', 'console'],
                message=texts.ALREADY_BUY
            )
        ]

    def to_representation(self, instance):
        request = self.context.get('request')
        return ShowConsoleAddedSerializer(
            instance.console,
            context={'request': request}
        ).data
