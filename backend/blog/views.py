from rest_framework.generics import get_object_or_404

from rest_framework import decorators, permissions, viewsets

from api.pagination import LimitPageNumberPagination
from api.permissions import IsAuthorOrAdminOrReadOnly
from .models import Post, Review
from .serializers import (PostReadSerializer, PostCreatedSerializer,
                          ReviewPostSerializer, CommentPostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для отображения постов.
    Для запросов на чтение используется PostReadSerializer
    Для запросов на изменение используется PostCreatedSerializer
    """
    queryset = Post.objects.all()
    serializer_class = PostReadSerializer
    pagination_class = LimitPageNumberPagination

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT', 'PATCH'):
            return PostCreatedSerializer
        return PostReadSerializer


class ReviewPostViewSet(viewsets.ModelViewSet):
    """Отображение действий с отзывами."""

    serializer_class = ReviewPostSerializer
    permission_classes = (IsAuthorOrAdminOrReadOnly,)

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().reviews_to_post.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, post=self.get_post()
        )


class CommentPostViewSet(viewsets.ModelViewSet):
    """Отображение действий с комментариями."""

    serializer_class = CommentPostSerializer
    permission_classes = (IsAuthorOrAdminOrReadOnly,)

    def get_review(self):
        return get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'),
        )

    def get_queryset(self):
        return self.get_review().comments_to_reviews.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, review=self.get_review()
        )
