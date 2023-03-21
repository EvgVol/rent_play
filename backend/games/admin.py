from django.contrib import admin

from .models import Game, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
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
        'tags'
    )
    list_filter = ('name', 'tags',)
    search_fields = ('name', 'tags')
