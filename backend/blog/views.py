from rest_framework.generics import get_object_or_404

from rest_framework import decorators, permissions, viewsets

from api.pagination import LimitPageNumberPagination
from api.permissions import IsAuthorOrAdminOrReadOnly
from .models import Post
from .serializers import PostReadSerializer, PostCreatedSerializer


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
    
