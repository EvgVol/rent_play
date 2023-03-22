from django.db import models

from core.enum import Limits


class TimeRent(models.Model):
    """Модель времени аренды"""

    name = models.CharField(
        'Наименование периода', 
        max_length=Limits.LENG_CUT.value,
        help_text='Введите название периода',
        unique=True,
        blank=False,
        null=False
    )

    value = models.CharField(
        'Значение', 
        max_length=Limits.LENG_CUT.value,
        help_text='Введите значение',
        unique=True,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'
        ordering = ('name',)
        constraints = [
            models.UniqueConstraint(fields=['name', 'value'],
                                    name='unique_timerent')
        ]
