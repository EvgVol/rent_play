from django.db import models
from django.core import validators


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
        upload_to='rent/',
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
