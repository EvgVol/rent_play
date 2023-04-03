from django.db import models, transaction
from django.shortcuts import get_object_or_404
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers, validators, exceptions, relations

from core import texts
from core.models import Period
from .models import Console, Favorite, ShoppingCart, Category, Review, RentalPrice
from users.serializers import UsersSerializer


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий."""

    class Meta:
        model = Category
        fields = '__all__'


class RentalPriceSerializers(serializers.ModelSerializer):
    """Сериализатор для вывода стоимости аренды."""
    
    id = serializers.PrimaryKeyRelatedField(queryset=Period.objects.all())

    class Meta:
        model = RentalPrice
        fields = ('id', 'price')


class ConsoleReadSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода консолей."""

    categories = CategorySerializer(many=True, read_only=True)
    author = UsersSerializer(read_only=True)
    image = Base64ImageField()
    is_rent = serializers.SerializerMethodField(read_only=True)
    rating = serializers.IntegerField(read_only=True)
    timeframe = RentalPriceSerializers(many=True,
                                       required=True,
                                       source='rental_price')

    class Meta:
        model = Console
        fields = (
            'id', 'categories', 'author', 'name', 'image', 'is_rent',
            'description', 'pub_date', 'rating', 'timeframe'
        )

    def get_is_rent(self,  obj):
        """Проверка - находится ли консоль в списке аренды."""
        return obj.rent_item.exists()

    def get_timeframe(self, console):
        """Получает список стоимости аренды."""
        return console.timeframe.values(
            'id',
            'name',
            price=models.F('consoles__rental_price')
        )


class ConsoleCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для размещения консолей."""

    author = UsersSerializer(read_only=True)
    categories = relations.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True)
    image = Base64ImageField(max_length=None, use_url=True)
    timeframe = RentalPriceSerializers(many=True)

    class Meta:
        model = Console
        fields = ('id', 'categories', 'name', 'image', 'description',
                  'barcode', 'author', 'timeframe')

    @transaction.atomic
    def create_bulk_timeframe(self, timeframe, console):
        for period in timeframe:
            RentalPrice.objects.get_or_create(
                console=console,
                period=period['id'],
                price=period['price']
            )

    @transaction.atomic
    def create(self, validated_data):
        timeframe_list = validated_data.pop('timeframe')
        categories = validated_data.pop('categories')
        author = self.context.get('request').user
        console = Console.objects.create(author=author, **validated_data)
        console.save()
        console.categories.set(categories)
        self.create_bulk_timeframe(timeframe_list, console)
        return console

    @transaction.atomic
    def update(self, instance, validated_data):
        categories = validated_data.pop('categories')
        timeframe = validated_data.pop('timeframe')
        instance.categories.clear()
        instance.categories.set(categories)
        instance.timeframe.clear()
        self.create_bulk_timeframe(console=instance,
                                   timeframe=timeframe)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return ConsoleReadSerializer(instance,
                                    context=context).data

    def validate(self, data):
        timeframe = self.initial_data.get('timeframe')
        categories = self.initial_data.get('categories')
        if not timeframe or not categories:
            raise serializers.ValidationError('Недостаточно данных')
        categories_list = []
        for tag in categories:
            if tag in categories_list:
                raise exceptions.ValidationError(
                    {'categories': texts.TAG_UNIQUE_ERROR}
                )
            categories_list.append(tag)
        return data

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return ConsoleReadSerializer(instance,
                                     context=context).data


class ReviewPostSerializer(serializers.ModelSerializer):
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
