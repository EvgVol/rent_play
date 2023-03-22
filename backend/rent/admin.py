from django.contrib import admin

from .models import TimeRent


@admin.register(TimeRent)
class TimeRentAdmin(admin.ModelAdmin):
    list_display = ('name', 'value',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('value',)
    empty_value_display = '-пусто-'
