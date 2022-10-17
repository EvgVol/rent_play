from django.contrib import admin

from .models import Console, Cost, RentalRate, Order

def view_cost_rent(self):
    return Cost.cost.filter('consol__period')

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

    


@admin.register(RentalRate)
class RentalRateAdmin(admin.ModelAdmin):
    """Админка срока аренды."""

    list_display = (
        'pk',
        'time',
    )
    empty_value_display = '-пусто-'


@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    """Админка стоимости арендной платы."""

    list_display = (
        'pk',
        'time',
        'console',
        'cost',
    )
    empty_value_display = '-пусто-'



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админка текущих заказов."""

    cost = view_cost_rent
    list_display = (
        'pk',
        'pub_date',
        'user',
        'console',
        'period',
        'cost',
    )
    ordering = ['-pub_date']
    readonly_fields = ('cost',)
