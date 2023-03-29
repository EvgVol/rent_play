from django.contrib import admin
from django.db.models import Avg

from .models import Console, Favorite, ShoppingCart, Category, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ('name', 'slug',)
    ordering = ('name',)


@admin.register(Console)
class ConsoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'categories', 'name', 'image', 
                    'description', 'barcode', 'count_favorites', 'status',
                    'rating')
    list_filter = ('name',)
    search_fields = ('name__startswith', )

    @admin.display(description='Количество в избранных')
    def count_favorites(self, obj):
        """Получаем количество избранных."""
        return obj.favorites.count()

    @admin.display(description='Статус')
    def status(self,  obj):
        """Получаем статус игровых консолей."""
        if obj.rent_item.exists():
            return 'Занята'
        return 'Свободна'

    @admin.display(description='Категории')
    def categories(self, obj):
        """Получаем категории."""
        return ', '.join(_.name for _ in obj.categories.all())

    @admin.display(description='Рейтинг')
    def rating(self, obj):
        return obj.reviews_console.all().aggregate(Avg('score'))['score__avg']
        

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Админка страницы отзывов."""

    list_display = (
        'pk', 'console', 'text',
        'author', 'score', 'pub_date',
    )
    search_fields = ('console', 'author', 'pub_date',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'console',)
    list_filter = ('user', 'console',)
    empty_value_display = '-пусто-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'console', )
    empty_value_display = '-пусто-'
