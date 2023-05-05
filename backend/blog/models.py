from django.db import models

from core.models import ReviewAndCommentModel, Product
from games.models import Game
from users.models import User


class Post(Product):
    """Параметры добавления новых постов."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )

    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        editable=False,
    )

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        verbose_name='Игра',
        help_text='Укажите игру',
    )

    class Meta(Product.Meta):
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        default_related_name = 'posts'
        constraints = (
            models.UniqueConstraint(
                fields=('name', 'author'),
                name='unique_author_post',
            ),
        )


class Review(ReviewAndCommentModel):
    """Модель отзыва."""

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )

    class Meta(ReviewAndCommentModel.Meta):
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        default_related_name = 'reviews_to_post'
        constraints = [
            models.UniqueConstraint(
                fields=('post', 'author',),
                name='unique_review_blog',
            )
        ]


class Comment(ReviewAndCommentModel):
    """Модель комментария к отзыву."""

    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='Отзыв'
    )

    class Meta(ReviewAndCommentModel.Meta):
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments_to_reviews'
