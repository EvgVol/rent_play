from django.core import validators
from django.db import models

from core.models import Product, ReviewAndCommentModel, Tags
from users.models import User


class Tag(Tags):
    """Модель тегов к играми."""

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'
        default_related_name = 'tags'


class Game(Product):
    """Модель игр."""

    tags = models.ManyToManyField(Tag, verbose_name='Теги')

    class Meta:
        verbose_name_plural = 'Игры'
        verbose_name = 'Игра'
        default_related_name = 'game'
        ordering = ('name',)


class FavoriteAndShoppingListModel(models.Model):
    """Абстрактная модель. Добавляет юзера и консоль."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Пользователь',
    )

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        verbose_name='Игра',
    )

    class Meta:
        abstract = True


class FavoriteGame(FavoriteAndShoppingListModel):
    """Модель игры в избранном."""

    class Meta(FavoriteAndShoppingListModel.Meta):
        verbose_name = 'Избранная игра'
        verbose_name_plural = 'Избранные игры'
        default_related_name = 'favorites_games'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'game',),
                name='unique_user_game',
            ),
        )

    def __str__(self):
        return f'Пользователь:{self.user} добавил {self.game} в избранное'


class ShoppingList(FavoriteAndShoppingListModel):
    """Модель добавление в корзину."""

    class Meta(FavoriteAndShoppingListModel.Meta):
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'
        default_related_name = 'shopping_list_games'
        constraints = [
            models.UniqueConstraint(fields=['user', 'game'],
                                    name='unique_shopping_list_games')
        ]

    def __str__(self):
        return f'Пользователь:{self.user} добавил {self.game} в бронь.'


class Review(ReviewAndCommentModel):
    """Модель отзыва к игре."""

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        verbose_name='Игра'
    )
    score = models.PositiveSmallIntegerField(
        'Оценка',
        db_index=True,
        validators=(
            validators.MinValueValidator(1),
            validators.MaxValueValidator(10)
        ),
        error_messages={
            'validators': 'Оценка от 1 до 10!'
        },
        default=1
    )

    class Meta(ReviewAndCommentModel.Meta):
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        default_related_name = 'reviews'
        constraints = [
            models.UniqueConstraint(
                fields=('game', 'author',),
                name='unique_review',
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
        default_related_name = 'comments'
