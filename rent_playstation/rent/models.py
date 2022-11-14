import datetime

from django.db import models
from django.conf import settings

from user.models import User


class AbstractConsoleAndGame(models.Model):
    """Абстрактный класс для консоли и игр."""

    title = models.CharField(
        'Наименовение',
        max_length=settings.LIMIT_LONG,
    )
    image = models.ImageField(
        'Изображение',
        upload_to='rent/',
        null=True,
        blank=True,
    )
    description = models.TextField('Описание')
    slug = models.SlugField('URL', unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title[:settings.LENG_CUT]


class Console(AbstractConsoleAndGame):
    """Модель игровых консолей."""

    FREE = 'free'
    RENT = 'rent'

    STATUS_CHOICES = [
        (FREE, 'Свободно'),
        (RENT, 'Арендовано'),
    ]

    barcode = models.TextField('Штрих-код')
    status = models.CharField(
        'Статус',
        max_length=max(len(status) for status, _ in STATUS_CHOICES),
        choices=STATUS_CHOICES,
        default=FREE,
        blank=True
    )

    class Meta(AbstractConsoleAndGame.Meta):
        verbose_name_plural = 'Консоли'
        verbose_name = 'Консоль'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'barcode'],
                name='unique_title_barcode',
            )
        ]

    @property
    def is_free(self):
        return self.status == self.FREE

    @property
    def is_rent(self):
        return self.status == self.RENT


class Game(models.Model):
    """Модель игр."""

    multu_user = models.BooleanField(
        'Многопользовательская',
        default=False
    )

    class Meta(AbstractConsoleAndGame.Meta):
        verbose_name_plural = 'Игры'
        verbose_name = 'Игра'


class RentPay(models.Model):
    """Модель арендной платы."""

    console = models.ForeignKey(
        Console,
        verbose_name='Приставка',
        on_delete=models.CASCADE,
        related_name='consoles',
        help_text='Выберите приставку',
    )














    # user = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name='client',
    #     default=User,
    #     verbose_name='Клиент'
    # )
    # console = models.ForeignKey(
    #     Console,
    #     verbose_name='Приставка',
    #     on_delete=models.CASCADE,
    #     related_name='consoles',
    #     help_text='Выберите приставку',
    # )
    # pub_date = models.DateTimeField(
    #     'Дата заказа',
    #     auto_now_add=True
    # )
    # created_at = models.DateField(
    #     'Дата начало аренды',
    #     help_text='Укажите начало даты аренды',
    #     default=datetime.date.today(),
    # )
    # updated_at = models.DateField(
    #     'Дата окончание аренды',
    #     help_text='Укажите окончание даты аренды',
    #     default=datetime.date.today(),
    # )

    # class Meta:
    #     verbose_name = 'Заказ'
    #     verbose_name_plural = 'Заказы'

    # def time_rent(self):
    #     if self.created_at == self.updated_at:
    #         return 1
    #     else:
    #         return (self.updated_at - self.created_at).days
    
    # def time(self):
    #     if self.time_rent() != 1:
    #         return 'суток'
    #     else:
    #         return 'сутки'

    # def __str__(self):
    #     return (f"Заказ №{self.id} от клиента {self.user} на аренду приставки {self.console} на {self.time_rent()} {self.time()}")
