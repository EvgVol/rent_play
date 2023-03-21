from django.urls import include, path
from rest_framework import routers

from users.views import CustomUserViewSet
from consoles.views import ConsoleViewSet 
from games.views import GameViewSet, TagViewSet


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'consoles', ConsoleViewSet, basename='consoles')
router.register(r'games', GameViewSet, basename='games')
router.register(r'tags', TagViewSet, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
