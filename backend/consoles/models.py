from django.db import models
from django.core import validators

from users.models import User


class Console(models.Model):
    """Модель игровых консолей."""

    name = models.CharField(
        'Наименовение',
        max_length=50,
    )
    image = models.ImageField(
        'Изображение',
        upload_to='consoles/',
        blank=False,
    )
    description = models.TextField('Описание')
    slug = models.SlugField('URL', unique=True, validators=[validators.validate_slug],)
    barcode = models.TextField('Штрих-код')

    class Meta:
        verbose_name_plural = 'Игровые приставки'
        verbose_name = 'Игровая приставка'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'barcode'],
                name='unique_name_barcode',
            )
        ]

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
        return f'Пользователь:{self.user} добавил {self.console} в бронь'
