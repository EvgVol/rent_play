from rest_framework import permissions


class IsAdmin(permissions.IsAdminUser):
    """Права администратора"""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_admin
        )

class IsModeratorOrAdminOrReadOnly(
    permissions.IsAuthenticatedOrReadOnly
):
    """Права для работы с играми."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_moderator
            or request.user.is_admin
        )

class IsModeratorOrAdminOrReadOnly(permissions.IsAdminUser):
    """Права для работы с игровыми приставками."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_rentor
            or request.user.is_admin
        )


class IsAuthorOrModeratorOrAdminOrReadOnly(
    permissions.IsAuthenticatedOrReadOnly
):
    """Права для работы с отзывами и комментариями."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_moderator
            or request.user.is_admin
        )
