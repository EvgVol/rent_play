from django.contrib import admin

from .models import User, Follow


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка Пользователей."""

    list_display = ('id', 'username', 'email', 'first_name', 'last_name',
                    'avatar', 'role', 'birthdate', 'is_staff', 'count_followers',)
    list_editable = ('role', 'is_staff')
    list_filter = ('username', 'role')
    search_fields = ('username', 'role')
    readonly_fields = ('count_followers',)

    @admin.display(description='Количество подписчиков')
    def count_followers(self, obj):
        """Получаем количество подписчиков."""
        return obj.follower.count()


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Админка подписчика."""

    list_display = ('user', 'author')
    list_filter = ('user', 'author')
    search_fields = ('user', 'author')
