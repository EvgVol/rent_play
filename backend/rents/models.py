from django.db import models
from django.core import validators

from users.models import User
from consoles.models import Console
from core.enum import Limits
from core import texts


class Rent(models.Model):
    """Модель аренды."""

    user = models.ForeignKey(
        User,
        verbose_name='Арендатель',
        on_delete=models.SET_NULL,
        null=True,
        related_name='leaser'
    )

    console = models.ForeignKey(
        Console,
        verbose_name='Приставка',
        on_delete=models.CASCADE,
        null=False,
        related_name='rent_item'
    )

    time = models.PositiveSmallIntegerField(
        'Время аренды в днях',
        default=Limits.TIME_MIN_AMOUNT.value,
        validators=[
            validators.MinValueValidator(
                Limits.TIME_MIN_AMOUNT.value,
                message=texts.TIME_MIN_AMOUNT_ERROR
            ),
        ],
    )

    pub_date = models.DateTimeField(
        verbose_name='Дата заказа',
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-pub_date',)

    def __str__(self):
        return f'Пользователь {self.user.username} забронировал {self.console} на {self.time} дней.'