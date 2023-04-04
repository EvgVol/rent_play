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
        two_week = Period.objects.filter(name='2 недели').values('value')[0]['value']
        one_day = Period.objects.filter(name='Сутки').values('value')[0]['value']
        seven_day = Period.objects.filter(name='Неделя').values('value')[0]['value']
        three_day = Period.objects.filter(name='Трое суток').values('value')[0]['value']
        timerent = (obj.end_date - obj.start_date).days

        if (obj.console.rental_price.filter(period=one_day).exists()and timerent < 3):
            return (obj.console.rental_price.filter(period=one_day).values('price')[0]['price']) * timerent
        
        elif obj.console.rental_price.filter(period=three_day).exists() and 3 < timerent > 7:
            return ((obj.console.rental_price.filter(period=three_day).values('price')[0]['price'])/3) * timerent
        
        elif obj.console.rental_price.filter(period=seven_day).exists() and 7 < timerent > 14:
            return ((obj.console.rental_price.filter(period=seven_day).values('price')[0]['price'])/7) * timerent
        
        elif obj.console.rental_price.filter(period=two_week).exists() and timerent > 14 :
            return ((obj.console.rental_price.filter(period=two_week).values('price')[0]['price'])/14) * timerent

        return obj.console.rental_price.filter(period__value=timerent).values('price')[0]['price']
        
        
        
        
        # timerent = (obj.end_date - obj.start_date).days
        # period_rent = obj.console.rental_price.filter(period__value=timerent)
        # if period_rent.exists():
        #     return period_rent.values('price')[0]['price']
        # if timerent < Period.objects.all()
        # return 52252: 2, 'price': 18000}, {