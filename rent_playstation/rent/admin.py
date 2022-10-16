from django.contrib import admin

from .models import Console, RentalRate, Order


@admin.register(Console)
class ConsoleAdmin(admin.ModelAdmin):
    """Админка существующих приставок."""

    list_display = (
        'pk',
        'title',
        'description',
        'slug',
        'image',
    )
    empty_value_display = '-пусто-'


@admin.register(RentalRate)
class RentalRateAdmin(admin.ModelAdmin):
    """Админка арендной платы."""

    list_display = (
        'pk',
        'console',
        'time',
        'cost',
    )
    empty_value_display = '-пусто-'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админка текущих заказов."""

    list_display = (
        'pk',
        'pub_date',
        'user',
        'console',
        'period',
    )
    ordering = ['-pub_date']
    empty_value_display = '-пусто-'
