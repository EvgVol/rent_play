from django.db import models, transaction
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers, validators, fields, relations

from core import texts
from core.models import Image
from .models import Console, Favorite, ShoppingCart, Category, ImagesInConsole
from users.serializers import UsersSerializer


class CategorySerializer(serializers.ModelSerializer):
    """Сериализхатор для категорий."""

    class Meta:
        model = Category
        fields = '__all__'


class ImagesInConsolSerializer(serializers.ModelSerializer):
    """Сериализатор для изображений в консоли"""

    id = serializers.PrimaryKeyRelatedField(
        read_only=True, source='ingredient'
    )
    name = serializers.SlugRelatedField(
        source='console',
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = ImagesInConsole
        fields = ('id',)


class ImagesInConsoleCreatedSerializer(serializers.ModelSerializer):
    """Сериализатор для изображений в консоли"""

    id = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all())

    class Meta:
        model = ImagesInConsole
        fields = ('id',)


class ConsoleReadSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода консолей."""

    categories = CategorySerializer(many=True, read_only=True)
    images = ImagesInConsolSerializer(many=True, required=True,
                                      source='console_images')
    is_rent = serializers.SerializerMethodField(read_only=True)

    def get_is_rent(self,  obj):
        """Проверка - находится ли консоль в списке аренды."""
        return obj.rent_item.exists()

    def get_images(self, console):
        """Получает список изображений для рецепта."""
        return console.images.filter(console=console)


class ConsoleCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для размещения консолей."""

    categories = relations.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True)
    images = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Console
        fields = ('id', 'categories', 'name', 'images', 'description', 'barcode',)


    @transaction.atomic
    def create_bulk_images(self, images, console):
        for image in images:
            ImagesInConsole.objects.get_or_create(
                console=console,
                image=image['id']
            )

    @transaction.atomic
    def update(self, instance, validated_data):
        categories = validated_data.pop('categories')
        images = validated_data.pop('images')
        instance.categories.clear()
        instance.categories.set(categories)
        instance.images.clear()
        self.create_bulk_images(console=instance, images=images)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return ConsoleReadSerializer(instance,
                                    context=context).data


class ShowConsoleAddedSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Console.
    Определён укороченный набор полей для некоторых эндпоинтов."""

    image = Base64ImageField()

    class Meta:
        model = Console
        fields = ('id', 'name', 'image', 'barcode',)


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
