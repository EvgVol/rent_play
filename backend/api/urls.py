from django.urls import include, path

from rest_framework import routers

from consoles.viewset import (CategoryViewSet, ConsoleViewSet,
                              ReviewConsoleViewSet)
from core.viewset import PeriodViewSet
from games.viewset import CommentViewSet, GameViewSet, ReviewViewSet, TagViewSet
from rents.viewset import RentViewSet
from users.viewset import CustomUserViewSet
from blog.viewset import PostViewSet, ReviewPostViewSet, CommentPostViewSet


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
router.register(r'posts/(?P<post_id>\d+)/reviews',
                ReviewPostViewSet,
                basename='reviewspost')
router.register(r'posts/(?P<post_id>\d+)/reviews/(?P<review_id>\d+)/comments',
                CommentPostViewSet,
                basename='commentspost')


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
