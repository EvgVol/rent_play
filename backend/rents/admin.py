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
        start_date = obj.console.rent_item.values_list('start_date')[0][0]
        and_date = 
        return start_date
        # return obj.console.rental_price.filter(period=time_rent).values_list('price')
        
        
        # return obj.console.timeframe.values('name', 'value', 'rental_price')