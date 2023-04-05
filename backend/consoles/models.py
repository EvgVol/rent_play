from django.core import validators
from django.db import models

from core import texts
from core.enum import Limits
from core.models import Period, Product, ReviewAndCommentModel, Tags
from users.models import User


class Category(Tags):
    """Модель категорий к консолям."""

    class Meta(Tags.Meta):
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        default_related_name = 'categories'


class Console(Product):
    """Модель игровых консолей."""

    author = models.ForeignKey(User, verbose_name='Арендодатель',
                               on_delete=models.CASCADE, null=True,)
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    barcode = models.TextField('Штрих-код')
    pub_date = models.DateTimeField(verbose_name='Дата размещения',
                                    auto_now_add=True, editable=False,)
    timeframe = models.ManyToManyField(Period, through='RentalPrice',
                                       verbose_name='Стоимость аренды')

    class Meta(Product.Meta):
        verbose_name_plural = 'Игровые приставки'
        verbose_name = 'Игровая приставка'
        default_related_name = 'consoles'
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'barcode'],
                name='unique_name_console',
            )
        ]


class RentalPrice(models.Model):
    """Модель стоимости аренды."""

    console = models.ForeignKey(Console,
                                verbose_name='Игровая консколь',
                                on_delete=models.CASCADE,
                                related_name='rental_price')

    period = models.ForeignKey(Period,
                               on_delete=models.CASCADE,
                               verbose_name='Период',
                               related_name='rental_price')

    price = models.PositiveSmallIntegerField(
        default=Limits.MIN_RENT.value,
        validators=(
            validators.MinValueValidator(
                Limits.MIN_RENT.value,
                message=texts.LOW_COST
            ),
        ),
        verbose_name='Стоимость аренды',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Стоимость'
        verbose_name_plural = 'Стоимость'
        constraints = [
            models.UniqueConstraint(
                fields=['period', 'console'],
                name='unique_period_console'
            )
        ]

    def __str__(self):
        return (
            f'{self.console.name} ({self.period.name}) - {self.price}'
        )


class Review(ReviewAndCommentModel):
    """Модель отзыва к игровой приставке."""

    console = models.ForeignKey(Console, on_delete=models.CASCADE,
                                verbose_name='Игровая приставка')
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
        default_related_name = 'reviews_console'
        constraints = [
            models.UniqueConstraint(
                fields=('console', 'author',),
                name='unique_review_console',
            )
        ]


class AbstractModelUserAndConsole(models.Model):
    """Абстрактная модель. Добавляет юзера и консоль."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Пользователь',
    )

    console = models.ForeignKey(
        Console,
        on_delete=models.CASCADE,
        verbose_name='Игровая приставка',
    )

    class Meta:
        abstract = True


class Favorite(AbstractModelUserAndConsole):
    """Модель приставки в избранном."""

    class Meta(AbstractModelUserAndConsole.Meta):
        verbose_name = 'Избранная консоль'
        verbose_name_plural = 'Избранные консоли'
        default_related_name = 'favorites'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'console',),
                name='unique_user_console',
            ),
        )

    def __str__(self):
        return f'Пользователь:{self.user} добавил {self.console} в избранное'


class ShoppingCart(AbstractModelUserAndConsole):
    """Модель приставки в корзине."""

    class Meta(AbstractModelUserAndConsole.Meta):
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронь'
        default_related_name = 'shopping_list'
        constraints = [
            models.UniqueConstraint(fields=['user', 'console'],
                                    name='unique_shopping')
        ]

    def __str__(self):
        return f'Пользователь:{self.user} добавил {self.console} в бронь'


class Like(AbstractModelUserAndConsole):
    """Модель лайка приставки."""

    class Meta(AbstractModelUserAndConsole.Meta):
        verbose_name = 'Нравится'
        verbose_name_plural = 'Нравится'
        default_related_name = 'console_like'
        constraints = [
            models.UniqueConstraint(fields=['user', 'console'],
                                    name='unique_like')
        ]

    def __str__(self):
        return (f'Пользователь:{self.user} поставил {self.console} отметку '
                '`Нравится`')


class Dislike(AbstractModelUserAndConsole):
    """Модель дизлайка приставки."""

    class Meta(AbstractModelUserAndConsole.Meta):
        verbose_name = 'Не нравится'
        verbose_name_plural = 'Не нравится'
        default_related_name = 'console_dislike'
        constraints = [
            models.UniqueConstraint(fields=['user', 'console'],
                                    name='unique_like')
        ]

    def __str__(self):
        return (f'Пользователь:{self.user} поставил {self.console} отметку '
                '`Не нравится`')
