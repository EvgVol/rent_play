from django.contrib import admin

from .models import Period

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')
