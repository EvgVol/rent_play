from django.db import models
from django.core import validators

from games.models import Game
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

    games = models.ManyToManyField(
        Game,
        through='GamesInRent',
        verbose_name='Игры',
        related_name='games_in_rent'
    )

    pub_date = models.DateTimeField(
        verbose_name='Дата заказа',
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        default_related_name = 'recipes'
        ordering = ('-pub_date',)
        constraints = (
            models.UniqueConstraint(
                fields=('name', 'author'),
                name='unique_for_author',
            ),
        )

    def __str__(self):
        return f'Пользователь {self.user.username} забронировал {self.console.name} на {self.time} дней'
    

class GamesInRent(models.Model):
    """Модель связывает Rent и Game."""

    rent = models.ForeignKey(
        Rent,
        verbose_name='Заказ',
        on_delete=models.CASCADE,
        related_name='game_list'
    )

    game =  models.ForeignKey(
        Game,
        verbose_name='Игра',
        on_delete=models.CASCADE,
        related_name='game_list'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Игра в заказе'
        verbose_name_plural = 'Игры в заказе'
        constraints = [
            models.UniqueConstraint(
                fields=['rent', 'game'],
                name='unique_rent_game'
            )
        ]

    def __str__(self):
        return (
            f'{self.rent.id} - {self.game.name}'
        )