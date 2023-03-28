from django.db import models
from django.core import validators

from users.models import User
from games.models import Game
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

    start_date = models.DateField(
        'Начало аренды',
        help_text='Укажите дату начала аренды',
    )

    end_date = models.DateField(
        'Конец аренды',
        help_text='Укажите дату окончание аренды',
    )

    pub_date = models.DateTimeField(
        verbose_name='Дата заказа',
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = [models.F('user').asc(nulls_last=True)]

    def time_rent(self):
        if self.end_date == self.start_date:
            return 1
        else:
            return self.end_date - self.start_date

    def __str__(self):
        return f'Пользователь {self.user.username} забронировал {self.console} на {self.time_rent()} дней.'
