from rest_framework import permissions


class IsAdmin(permissions.IsAdminUser):
    """Права администратора"""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_staff
        )


class IsModeratorOrAdminOrReadOnly(permissions.IsAdminUser):
    """Права для работы с игровыми приставками."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_rentor
            or request.user.is_staff
        )

