from django.db import models
from django.core import validators

from users.models import User
from core.models import ImageAlbum



class Console(models.Model):
    """Модель игровых консолей."""

    lessor = models.ForeignKey(User, verbose_name='Арендодатель',
                               on_delete=models.CASCADE,)
    name = models.CharField('Наименовение', max_length=50,)
    album = models.OneToOneField(ImageAlbum,
                                 verbose_name='Изображения',
                                 related_name='model',
                                 on_delete=models.CASCADE)
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


class Image(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Console, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='consoles/')
    default = models.BooleanField(default=False)

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
