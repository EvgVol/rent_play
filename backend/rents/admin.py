from django.contrib import admin

from .models import Rent
from core.models import Period


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'start_date', 'end_date', 'user',
                    'console', 'get_rentor', 'time_rent', 'get_price')
    list_filter = ('console',)
    search_fields = ('console',)
    empty_value_display = '-пусто-'

    @admin.display(description='Арендодатель')
    def get_rentor(self, obj):
        return obj.console.author

    @admin.display(description='Цена')
    def get_price(self, obj):
        return obj.console.rental_price.values('period__value') 