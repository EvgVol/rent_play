import datetime
from email import message
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Console(models.Model):
    """Модель игровых консолей."""

    STATUS_CHOICES = [
        ('F', 'Свободно'),
        ('R', 'Арендовано'),
    ]

    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('URL', unique=True)
    description = models.TextField('Описание')
    image = models.ImageField(
        'Изображение',
        upload_to='rent/',
        null=True,
        blank=True
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

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
        blank=True,
        null=True,
        help_text='Выберите приставку'
    )
    pub_date = models.DateTimeField(
        'Дата заказа',
        auto_now_add=True
    )
    created_at = models.DateField(
        'Дата начало аренды',
        blank=True,
        help_text='Укажите начало даты аренды',
        default=datetime.date.today
    )
    updated_at = models.DateField(
        'Дата окончание аренды',
        blank=True,
        help_text='Укажите окончание даты аренды',
        default=datetime.date.today
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def time_rent(self):
        if self.created_at == self.updated_at:
            return self.created_at
        else:
            return self.updated_at - self.created_at

    def __str__(self):
        return (f"Заказ №'{self.id}' от клиента '{self.user}' на аренду приставки '{self.console}' на время '{self.time_rent()}'")
