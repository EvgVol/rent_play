from django.contrib import admin

from .models import Console


@admin.register(Console)
class ConsoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'slug', 'barcode', 'status', )
    readonly_fields = ('status',)
    list_filter = ('name', )
    search_fields = ('name__startswith', )