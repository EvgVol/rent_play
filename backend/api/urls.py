from django.urls import include, path

from rest_framework import routers

from consoles.views import (CategoryViewSet, ConsoleViewSet,
                            ReviewConsoleViewSet)
from core.views import PeriodViewSet
from games.views import CommentViewSet, GameViewSet, ReviewViewSet, TagViewSet
from rents.views import RentViewSet
from users.views import CustomUserViewSet
from blog.views import PostViewSet


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
router.register(r'periods', PeriodViewSet, basename='periods')
router.register(r'posts', PostViewSet, basename='posts')


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
