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
    description = models.TextField('Штрих-код')
    image = models.ImageField(
        'Изображение',
        upload_to='rent/',
        null=True,
        blank=True,
    )
    price_one_day = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        verbose_name='Стоимость за 1 день'
    )
    price_two_day = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        verbose_name='Стоимость за 2 дня'
    )
    price_three_day = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        verbose_name='Стоимость за 3 дня'
    )
    price_four_day = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        verbose_name='Стоимость за 4 дня'
    )
    price_five_day = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        verbose_name='Стоимость за 5 дней'
    )
    price_six_day = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        verbose_name='Стоимость за 6 дней'
    )
    price_week_day = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        verbose_name='Стоимость за неделю'
    )
    price_prolongation = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        verbose_name='Стоимость за продление'
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