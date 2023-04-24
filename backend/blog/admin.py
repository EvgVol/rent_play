from django.contrib import admin

from .models import Post, Review, Comment


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'post', 'text',
        'author', 'score', 'pub_date',
    )
    search_fields = ('post', 'author', 'pub_date',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'review', 'text',
        'author', 'pub_date',
    )
    search_fields = ('review', 'author', 'pub_date',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('pk', 'name', 'pub_date', 'author', 'description',
                    'game', 'get_genre', 'get_tags')
    search_fields = ('description', )
    list_filter = ('pub_date', )
    empty_value_display = '-пусто-'

    @admin.display(description='Жанр')
    def get_genre(self, obj):
        """Получаем жанр."""
        return obj.game.genres.all()[0]

    @admin.display(description='Теги')
    def get_tags(self, obj):
        """Получаем тег."""
        return obj.game.tags.all()[0]
