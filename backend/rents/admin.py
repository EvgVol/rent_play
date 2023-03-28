from django.contrib import admin

from .models import Rent


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'start_date', 'end_date', 'user', 'console',)
    list_filter = ('console',)
    search_fields = ('console',)
    empty_value_display = '-пусто-'
