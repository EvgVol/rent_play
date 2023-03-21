from django.db import models

from users.models import User
from consoles.models import Console


class Lease(models.Model):
    """Модель аренды."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='leaser',
        verbose_name='Арендатор',
    )

    console = models.ForeignKey(
        Console,
        on_delete=models.CASCADE,
        related_name='console',
        verbose_name='Игровая приставка'
    )

    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренды'
        ordering = ('user',)
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'console'],
                name='unique_lease'
            ),
            models.CheckConstraint(
                check=~models.Q(console=models.F('user')),
                name='no_self_lease'
            )
        ]

    def __str__(self):
        return f'Пользователь {self.user} арендовал {self.console}'
