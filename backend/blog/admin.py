from django.contrib import admin

from .models import Post, Genre


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Post)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'text',
        'author', 'score', 'pub_date',
    )
    search_fields = ('title', 'author', 'pub_date',)
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