from django.db import models
from django.core import validators
from colorfield.fields import ColorField

from core.enum import Limits, Regex
from core import texts
from users.models import User


class Tag(models.Model):
    """Модель тегов к играми."""

    name = models.CharField(
        'Наименовение',
        max_length=Limits.MAX_LEN_TAG.value,
        unique=True,
        help_text=texts.WARNING_LIMIT_CHAR,
    )

    color = ColorField(
        'Цветовой HEX-код',
        unique=True,
        default='#FF0000',
        max_length=Limits.LENG_COLOR.value,
        validators=[
            validators.RegexValidator(
                regex=Regex.COLOR_REGEX,
                message=texts.NOT_COLOR_HEX
            ),
        ],
        error_messages={'unique': texts.COLOR_NO_UNIQUE},
        help_text=texts.HELP_CHOISE_COLOR
    )
    slug = models.SlugField('URL', unique=True,
                            validators=[validators.validate_slug],)

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'

    def __str__(self):
        return self.name


class Game(models.Model):
    """Модель игр."""

    name = models.CharField('Наименовение',
                            max_length=Limits.MAX_LEN_TAG.value,)
    image = models.ImageField('Изображение', upload_to='games/',
                              null=True, blank=True,)
    description = models.TextField('Описание')
    slug = models.SlugField('URL', unique=True,
                            validators=[validators.validate_slug],)
    tags = models.ManyToManyField(Tag, verbose_name='Теги')

    class Meta:
        verbose_name_plural = 'Игры'
        verbose_name = 'Игра'

    def __str__(self):
        return self.name


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
        return f'Пользователь:{self.user} добавил {self.game} в корзину'


class ReviewAndCommentModel(models.Model):
    """Абстрактная модель. Добавляет текст, автора и дату публикации."""

    text = models.CharField(
        'Текст отзыва',
        max_length=Limits.LENG_MAX_REVIEW.value,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    pub_date = models.DateTimeField(
        'Дата публикации отзыва',
        auto_now_add=True,
    )

    class Meta:
        abstract = True
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:Limits.LENG_CUT.value]


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
