from django.db import transaction
from django.shortcuts import get_object_or_404
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers, validators, exceptions, relations

from core import texts
from .models import Console, Favorite, ShoppingCart, Category, Review
from users.serializers import UsersSerializer


class CategorySerializer(serializers.ModelSerializer):
    """Сериализхатор для категорий."""

    class Meta:
        model = Category
        fields = '__all__'


class ConsoleReadSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода консолей."""

    categories = CategorySerializer(many=True, read_only=True)
    author = UsersSerializer(read_only=True)
    image = Base64ImageField()
    is_rent = serializers.SerializerMethodField(read_only=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Console
        fields = (
            'id', 'categories', 'author', 'name', 'image', 'is_rent',
            'description', 'pub_date', 'rating',
        )

    def get_is_rent(self,  obj):
        """Проверка - находится ли консоль в списке аренды."""
        return obj.rent_item.exists()


class ConsoleCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для размещения консолей."""

    author = UsersSerializer(read_only=True)
    categories = relations.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True)
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Console
        fields = ('id', 'categories', 'name', 'image', 'description',
                  'barcode', 'author',)

    @transaction.atomic
    def create(self, validated_data):
        categories = validated_data.pop('tags')
        author = self.context.get('request').user
        console = Console.objects.create(author=author, **validated_data)
        console.save()
        console.categories.set(categories)
        return console

    @transaction.atomic
    def update(self, instance, validated_data):
        categories = validated_data.pop('categories')
        instance.categories.clear()
        instance.categories.set(categories)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return ConsoleReadSerializer(instance,
                                    context=context).data

    def validate_categories(self, value):
        """Проверяем на наличие уникального тега."""
        categories = value
        if not categories:
            raise exceptions.ValidationError(
                {'categories': texts.TAG_ERROR}
            )
        categories_list = []
        for tag in categories:
            if tag in categories_list:
                raise exceptions.ValidationError(
                    {'categories': texts.TAG_UNIQUE_ERROR}
                )
            categories_list.append(tag)
        return value

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return ConsoleReadSerializer(instance,
                                     context=context).data


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
            console_id = self.context['view'].kwargs.get('console_id')
            console = get_object_or_404(Console, pk=console_id)
            if Review.objects.filter(
                    author=request.user, console=console
            ).exists():
                raise serializers.ValidationError(
                    'Вы уже оставили отзыв!')
        return data


class ShowConsoleAddedSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Console.
    Необходим для отражения приставки в избранном и списке покупок.
    """

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
