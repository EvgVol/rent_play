from django.db import models
from django.core import validators

from users.models import User


class Console(models.Model):
    """Модель игровых консолей."""

    FREE = 'free'
    RENT = 'rent'

    STATUS_CHOICES = [
        (FREE, 'Свободно'),
        (RENT, 'Арендовано'),
    ]

    name = models.CharField(
        'Наименовение',
        max_length=50,
    )
    image = models.ImageField(
        'Изображение',
        upload_to='consoles/',
        null=True,
        blank=True,
    )
    description = models.TextField('Описание')
    slug = models.SlugField('URL', unique=True, validators=[validators.validate_slug],)
    barcode = models.TextField('Штрих-код')
    status = models.CharField(
        'Статус',
        max_length=max(len(status) for status, _ in STATUS_CHOICES),
        choices=STATUS_CHOICES,
        default=FREE,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Консоли'
        verbose_name = 'Консоль'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'barcode'],
                name='unique_name_barcode',
            )
        ]

    @property
    def is_free(self):
        return self.status == self.FREE

    @property
    def is_rent(self):
        return self.status == self.RENT

    def __str__(self):
        return self.name


class FavoriteAndShoppingCartModel(models.Model):
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


class Favorite(FavoriteAndShoppingCartModel):
    """Модель приставки в избранном."""

    class Meta(FavoriteAndShoppingCartModel.Meta):
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


class ShoppingCart(FavoriteAndShoppingCartModel):
    """Модель приставки в корзине."""

    class Meta(FavoriteAndShoppingCartModel.Meta):
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронь'
        default_related_name = 'shopping_list'
        constraints = [
            models.UniqueConstraint(fields=['user', 'console'],
                                    name='unique_shopping')
        ]

    def __str__(self):
        return f'Пользователь:{self.user} добавил {self.console} в корзину'
