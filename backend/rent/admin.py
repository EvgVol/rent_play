from django.contrib import admin

from .models import GamesInRent, Rent


class GamesInRentInline(admin.TabularInline):
    model = GamesInRent
    extra = 2
    min_num = 1


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'user', 'console', 'time', 'get_games',)
    list_filter = ('console',)
    # search_fields = ('console', 'user__email', 'game__name')
    empty_value_display = '-пусто-'
    inlines = (GamesInRentInline,)

    @admin.display(description='Игры')
    def get_games(self, obj):
        """Получаем игры."""
        return '\n '.join([
            f'{game["game__name"]}'
            for game in obj.game_list.values('game__name')
        ])
    