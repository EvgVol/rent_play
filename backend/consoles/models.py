from django.db import models


class AbstractConsoleAndGame(models.Model):
    """Абстрактный класс для консоли и игр."""

    title = models.CharField(
        'Наименовение',
        max_length=50,
    )
    image = models.ImageField(
        'Изображение',
        upload_to='rent/',
        null=True,
        blank=True,
    )
    description = models.TextField('Описание')
    slug = models.SlugField('URL', unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Console(AbstractConsoleAndGame):
    """Модель игровых консолей."""

    FREE = 'free'
    RENT = 'rent'

    STATUS_CHOICES = [
        (FREE, 'Свободно'),
        (RENT, 'Арендовано'),
    ]

    barcode = models.TextField('Штрих-код')
    status = models.CharField(
        'Статус',
        max_length=max(len(status) for status, _ in STATUS_CHOICES),
        choices=STATUS_CHOICES,
        default=FREE,
        blank=True
    )

    class Meta(AbstractConsoleAndGame.Meta):
        verbose_name_plural = 'Консоли'
        verbose_name = 'Консоль'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'barcode'],
                name='unique_title_barcode',
            )
        ]

    @property
    def is_free(self):
        return self.status == self.FREE

    @property
    def is_rent(self):
        return self.status == self.RENT


class Game(AbstractConsoleAndGame):
    """Модель игр."""

    multu_user = models.BooleanField(
        'Многопользовательская',
        default=False
    )

    class Meta(AbstractConsoleAndGame.Meta):
        verbose_name_plural = 'Игры'
        verbose_name = 'Игра'
