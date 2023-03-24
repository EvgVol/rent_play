from django.contrib import admin

from .models import Console, Favorite, ShoppingCart


@admin.register(Console)
class ConsoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'slug', 'barcode', 'count_favorites' )
    list_filter = ('name', )
    search_fields = ('name__startswith', )

    @admin.display(description='Количество в избранных')
    def count_favorites(self, obj):
        """Получаем количество избранных."""
        return obj.favorites.count()

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'console',)
    list_filter = ('user', 'console',)
    empty_value_display = '-пусто-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'console', )
    empty_value_display = '-пусто-'
