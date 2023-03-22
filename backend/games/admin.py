from django.contrib import admin

from .models import Game, Tag, Comment, Review, FavoriteGame, ShoppingList


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Админка страницы тегов."""

    list_display = ('id', 'name', 'color', 'slug',)
    search_fields = ('name', 'slug',)
    ordering = ('name',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Админка страницы игр."""

    list_display = (
        'id',
        'name',
        'image',
        'description',
        'slug',
        'get_tags'
    )
    list_filter = ('name', 'tags',)
    search_fields = ('name',)

    @admin.display(description='Тэги')
    def get_tags(self, obj):
        """Получаем теги."""
        return ', '.join(_.name for _ in obj.tags.all())


@admin.register(FavoriteGame)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'game',)
    list_filter = ('user', 'game',)
    empty_value_display = '-пусто-'


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', )
    empty_value_display = '-пусто-'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Админка страницы отзывов."""

    list_display = (
        'pk', 'game', 'text',
        'author', 'score', 'pub_date',
    )
    search_fields = ('game', 'author', 'pub_date',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Админка страницы комментариев."""

    list_display = (
        'pk', 'review', 'text',
        'author', 'pub_date',
    )
    search_fields = ('review', 'author', 'pub_date',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
