from django.contrib import admin

from .models import Period


@admin.register(Period)
class PeridAdmin(admin.ModelAdmin):
    field = ('start_date', 'end_date',)