from django.contrib.auth import get_user_model
from django.db import models

from core.models import Tags, ReviewAndCommentModel, Product


User = get_user_model()


class Genre(Tags):
    """Модель жанра"""

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Post(Product):
    """Параметры добавления новых постов."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Жанр',
        help_text='Укажите жанр'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        default_related_name = 'posts'


class Comment(ReviewAndCommentModel):
    """Модель комментария."""

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )

    class Meta(ReviewAndCommentModel.Meta):
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'blog_comments'
