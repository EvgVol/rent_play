from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

STATUS_CHOICES = [
    ('F', 'Свободно'),
    ('R', 'Арендовано'),
]

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
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name_plural = 'Консоли'
        verbose_name = 'Консоль'

    def __str__(self):
        return self.title[:30]


class RentalRate(models.Model):
    """Модель срока аренды."""

    time = models.CharField('Срок аренды', max_length=50)

    class Meta:
        verbose_name = 'Срок'
        verbose_name_plural = 'Сроки'
    
    def __str__(self):
        return self.time


class Cost(models.Model):
    """Модель стоимости аренды."""
    time = models.ForeignKey(
        RentalRate,
        verbose_name='Срок арендной платы',
        on_delete=models.CASCADE
    )
    cost = models.PositiveIntegerField('Стоимость')
    console = models.ForeignKey(
        Console,
        on_delete=models.CASCADE,
        verbose_name='Консоль'
    )

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
    
    def __int__(self):
        return self.cost

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
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text='Выберите приставку'
    )
    pub_date = models.DateTimeField(
        'Дата заказа',
        auto_now_add=True
    )
    cost = models.ForeignKey(
        Cost,
        verbose_name='Стоимость',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return (f"Клиент: '{self.user}' - дата заказа: '{self.pub_date}'- приставка: '{self.console}' - срок аренды '{self.period}'")
