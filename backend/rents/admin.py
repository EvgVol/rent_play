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
        # time_rent = (obj.end_date - obj.start_date).days
        # price = obj.console.timeframe['price']
        timerent = (obj.end_date - obj.start_date).days
        period_rent = obj.console.rental_price.filter(period__value=timerent)
        if period_rent.exists():
            return period_rent.values('price')[0]['price']
        return 52252

        
        
        # return obj.console.timeframe.values('name', 'value', 'rental_price')