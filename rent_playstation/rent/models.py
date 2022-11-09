import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.core.validators import (MaxValueValidator,
                                    MinValueValidator,
                                    validate_slug)

User = get_user_model()


class Console(models.Model):
    """Модель игровых консолей."""

    FREE = 'Свободно'
    RENT = 'Занято'

    STATUS_CHOICES = [
        (FREE, 'Свободно'),
        (RENT, 'Арендовано'),
    ]

    console = models.CharField(
        'Наименовение консоли',
        max_length=settings.LIMIT_LONG = 200,
    )
    slug = models.SlugField('URL', unique=True)
    barcode = models.TextField('Штрих-код')
    image = models.ImageField(
        'Изображение',
        upload_to='rent/',
        null=True,
        blank=True,
    )
    status = models.CharField(
        'Статус',
        max_length=max(len(status) for status, _ in STATUS_CHOICES)
        choices=STATUS_CHOICES,
        default=FREE,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Консоли'
        verbose_name = 'Консоль'
        constraints = [
            models.UniqueConstraint(
                fields=['console', 'barcode'],
                name='unique_console_barcode',
            )
        ]

    @property
    def is_free(self):
        return self.status == self.FREE

    @property
    def is_rent(self):
        return self.status == self.RENT

    def __str__(self):
        return f'Консоль {self.console}, штрих код: {self.barcode}'


class Game(models.Model):
    title = models.CharField(
        'Наименовение игры',
        max_length=settings.LIMIT_LONG = 200
    )
    description = 

class Order(models.Model):
    """Модель заказа приставки."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='client',
        default=User,
        verbose_name='Клиент'
    )
    console = models.ForeignKey(
        Console,
        verbose_name='Приставка',
        on_delete=models.CASCADE,
        null=True,
        related_name='consoles',
        help_text='Выберите приставку',
    )
    pub_date = models.DateTimeField(
        'Дата заказа',
        auto_now_add=True
    )
    created_at = models.DateField(
        'Дата начало аренды',
        help_text='Укажите начало даты аренды',
        default=datetime.date.today(),
    )
    updated_at = models.DateField(
        'Дата окончание аренды',
        help_text='Укажите окончание даты аренды',
        default=datetime.date.today(),
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def time_rent(self):
        if self.created_at == self.updated_at:
            return 1
        else:
            return (self.updated_at - self.created_at).days
    
    def time(self):
        if self.time_rent() != 1:
            return 'суток'
        else:
            return 'сутки'

    def __str__(self):
        return (f"Заказ №{self.id} от клиента {self.user} на аренду приставки {self.console} на {self.time_rent()} {self.time()}")


# def get_time():
#     days = (Order().time_rent())
#     # console_client = (Order().)
#     return Order().objects.get().all


# get_time() 