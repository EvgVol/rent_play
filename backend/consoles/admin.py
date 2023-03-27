from django.contrib import admin

from .models import Console, Favorite, ShoppingCart, ImagesInConsole, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ('name', 'slug',)
    ordering = ('name',)


class ImagesInConsoleInline(admin.TabularInline):
    model = ImagesInConsole
    extra = 2
    min_num = 1


@admin.register(Console)
class ConsoleAdmin(admin.ModelAdmin):
    list_display = ('lessor', 'categories', 'name', 'get_images', 'description', 'barcode', 'count_favorites', 'status')
    list_filter = ('lessor', 'name')
    search_fields = ('name__startswith', )
    inlines = (ImagesInConsoleInline,)
    

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

    @admin.display(description='Изображения')
    def get_images(self, obj):
        """Получаем ингредиенты."""
        return '\n '.join([
            f'{img["image__name"]}'
            for img in obj.console_images.all()])

    @admin.display(description='Категории')
    def categories(self, obj):
        """Получаем категории."""
        return ', '.join(_.name for _ in obj.categories.all())
        

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'console',)
    list_filter = ('user', 'console',)
    empty_value_display = '-пусто-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'console', )
    empty_value_display = '-пусто-'


@admin.register(ImagesInConsole)
class ImagesInConsoleAdmin(admin.ModelAdmin):
    pass