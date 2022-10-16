from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Console(models.Model):
    """Модель игровых консолей."""

    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('URL', unique=True)
    description = models.TextField('Описание')
    image = models.ImageField(
        'Изображение',
        upload_to='rent/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Консоли'
        verbose_name = 'Консоль'

    def __str__(self):
        return self.text[:15]


class RentalRate(models.Model):
    """Модель арендной платы."""

    time = models.CharField('Срок аренды', max_length=50)
    cost = models.PositiveIntegerField('Стоимость')
    console = models.ForeignKey(
        Console,
        on_delete=models.CASCADE,
        verbose_name='Консоль'
    )

    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренды'


class Order(models.Model):
    """Модель заказа приставки."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='client'
    )
    period = models.ForeignKey(
        RentalRate,
        verbose_name='Срок аренды',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='Укажите срок аренды'
    )
    console = models.ForeignKey(
        Console,
        verbose_name='Приставка',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='Выберите приставку'
    )
    pub_date = models.DateTimeField(
        'Дата заказа',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return (f"Клиент: '{self.user}' - дата заказа: '{self.pub_date}'- приставка: '{self.console}' - срок аренды '{self.period}'")
