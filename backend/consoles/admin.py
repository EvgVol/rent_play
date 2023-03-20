from django.contrib import admin

from .models import Console, Game


@admin.register(Console)
class ConsoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'slug', 'barcode', 'status', )
    readonly_fields = ('status',)
    list_filter = ('title', )
    search_fields = ('title__startswith', )
    

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'slug', 'multu_user', )
    list_filter = ('title', )
    search_fields = ('title__startswith', )