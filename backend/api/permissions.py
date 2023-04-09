from rest_framework import permissions


class IsAuthorOrAdminOrReadOnly(
    permissions.IsAuthenticatedOrReadOnly
):
    """Права для работы с отзывами и комментариями."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_admin
        )


class IsRentorOrAdminOrReadOnly(permissions.BasePermission):
    """Права для работы с игровыми приставками."""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_rentor
            or request.user.is_staff
        )

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user.is_rentor
                or request.user.is_staff)
