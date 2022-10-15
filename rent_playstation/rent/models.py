from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Rental_rate(models.Model):
    """Модель арендной платы."""

    time = models.CharField('Срок аренды', max_length=50)
    cost = models.PositiveIntegerField()


class Console(models.Model):
    """Модель игровых приставок."""

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
        verbose_name_plural = 'Приставки'
        verbose_name = 'Приставка'

    def __str__(self):
        return self.text[:15]


class Order(models.Model):
    """Модель заказа приставки."""

    period = models.ForeignKey(
        Rental_rate,
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
