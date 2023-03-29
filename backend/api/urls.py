from django.urls import include, path
from rest_framework import routers

from users.views import CustomUserViewSet
from consoles.views import (ConsoleViewSet, CategoryViewSet,
                            ReviewConsoleViewSet)
from games.views import (GameViewSet, TagViewSet, ReviewViewSet,
                         CommentViewSet)
from rents.views import RentViewSet

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'consoles', ConsoleViewSet, basename='consoles')
router.register(r'consoles/(?P<console_id>\d+)/reviews',
                ReviewConsoleViewSet, basename='reviewsconsole')
router.register(r'games', GameViewSet, basename='games')
router.register(r'games/(?P<game_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'games/(?P<game_id>\d+)/reviews/(?P<review_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'rents', RentViewSet, basename='rents')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
