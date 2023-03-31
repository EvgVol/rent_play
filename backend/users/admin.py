from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка Пользователей."""

    list_display = ('id', 'username', 'email', 'first_name', 'last_name',
                    'avatar', 'role', 'birthdate', 'is_staff')
    list_editable = ('role', 'is_staff')
    list_filter = ('username', 'role')
    search_fields = ('username', 'role')
