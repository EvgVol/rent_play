from django.contrib import admin

from .models import Period, Feedback


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Админ-панель модели профиля."""

    list_display = ('email', 'ip_address', 'user')
    list_display_links = ('email', 'ip_address')
