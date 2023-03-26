from django.db import models
from django.core import validators
from django.utils.safestring import mark_safe

from users.models import User
from core.models import Image


class Console(models.Model):
    """Модель игровых консолей."""

    lessor = models.ForeignKey(User, verbose_name='Арендодатель',
                               on_delete=models.CASCADE,)
    name = models.CharField('Наименовение', max_length=50,)
    images = models.ManyToManyField(Image, through='ImagesInConsole', verbose_name='Изображения')
    description = models.TextField('Описание')
    slug = models.SlugField('URL', unique=True,
                            validators=[validators.validate_slug],)
    barcode = models.TextField('Штрих-код')
    pub_date = models.DateTimeField(verbose_name='Дата размещения',
                                    auto_now_add=True, editable=False,)

    class Meta:
        verbose_name_plural = 'Игровые приставки'
        verbose_name = 'Игровая приставка'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'barcode', 'lessor'],
                name='unique_name_barcode',
            )
        ]

    def __str__(self):
        return self.name


class ImagesInConsole(models.Model):
    console = models.ForeignKey(
        Console,
        verbose_name='Приставка',
        on_delete=models.CASCADE,
        related_name='console_images'
    )
    image = models.ForeignKey(
        Image,
        verbose_name='Изображение',
        on_delete=models.CASCADE,
        related_name='console_images'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения '
        constraints = [
            models.UniqueConstraint(
                fields=['console', 'image'],
                name='unique_console_image'
            )
        ]

    def __str__(self):
        return (
            f'В {self.console.name} добавлена {self.image.name}'
        )


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
