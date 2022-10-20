import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Console(models.Model):
    """Модель игровых консолей."""

    STATUS_CHOICES = [
        ('F', 'Свободно'),
        ('R', 'Арендовано'),
    ]

    title = models.CharField(
        'Название',
        max_length=200,
    )
    slug = models.SlugField('URL', unique=True)
    description = models.TextField('Описание')
    image = models.ImageField(
        'Изображение',
        upload_to='rent/',
        null=True,
        blank=True,
    )
    status = models.CharField(
        'Статус',
        max_length=1,
        choices=STATUS_CHOICES,
        default='F',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = 'Консоли'
        verbose_name = 'Консоль'

    def __str__(self):
        return self.title[:20]


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
            return f'{1} сутки'
        else:
            return f'{(self.updated_at - self.created_at).days} суток'

    def __str__(self):
        return (f"Заказ №{self.id} от клиента {self.user} на аренду приставки {self.console} на {self.time_rent()}")