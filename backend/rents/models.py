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

    games = models.ManyToManyField(
        Game,
        through='GameInRent',
        verbose_name='Игры',
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
        ordering = [models.F('user').asc(nulls_last=True)]

    def __str__(self):
        return f'Пользователь {self.user.username} забронировал {self.console} на {self.time} дней.'
    
    
class GameInRent(models.Model):
    """Игры в заказе."""

    rent = models.ForeignKey(
        Rent,
        verbose_name='Заказ',
        on_delete=models.CASCADE,
        related_name='game_list'
    )
    game = models.ForeignKey(
        Game,
        verbose_name='Игра',
        on_delete=models.CASCADE,
        related_name='game_list'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        constraints = [
            models.UniqueConstraint(
                fields=['game', 'rent'],
                name='unique_game_rent'
            )
        ]

    def __str__(self):
        return self.game.name
