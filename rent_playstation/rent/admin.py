from django.contrib import admin
from django.shortcuts import get_object_or_404

from .models import Console, Order


@admin.register(Console)
class ConsoleAdmin(admin.ModelAdmin):
    """Админка существующих приставок."""

    list_display = (
        'pk',
        'title',
        'description',
        'slug',
        'image',
        'status'
    )
    list_editable = ['status']
    # empty_value_display = '-пусто-'
    actions = ['make_rented', 'make_free']
    list_filter = ('title', )
    search_fields = ("title__startswith", )
    
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.status == 'Свободно':
    #         kwargs['empty_label'] = '-пусто-'
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    @admin.action(description='Свободно')
    def make_free(self, request, queryset):
        queryset.update(status='F')
    
    @admin.action(description='В аренде')
    def make_rented(modeladmin, request, queryset):
        queryset.update(status='R')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админка текущих заказов."""
    
    list_display = (
        'pk',
        'user',
        'pub_date',
        'console',
        'created_at',
        'updated_at'
    )
    ordering = ['-pub_date']
    # readonly_fields = ('user',)

