from django.urls import include, path
from rest_framework import routers

from .views import CustomUserViewSet, ConsoleViewSet, GameViewSet


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'consoles', ConsoleViewSet, basename='consoles')
router.register(r'games', GameViewSet, basename='games')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
