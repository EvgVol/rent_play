from colorfield.fields import ColorField
from django.core import validators
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import localtime
from django.utils.translation import gettext as _

from . import texts
from .enum import Limits, Regex
from .validators import validate_not_empty


User = get_user_model()


class Tags(models.Model):
    """Абстрактная модель тегов."""

    name = models.CharField(
        'Наименовение',
        max_length=Limits.MAX_LEN_TAG.value,
        unique=True,
        help_text=texts.WARNING_LIMIT_CHAR,
    )

    color = ColorField(
        'Цветовой HEX-код',
        unique=True,
        default='#FF0000',
        max_length=Limits.LENG_COLOR.value,
        validators=[
            validators.RegexValidator(
                regex=Regex.COLOR_REGEX,
                message=texts.NOT_COLOR_HEX
            ),
        ],
        error_messages={'unique': texts.COLOR_NO_UNIQUE},
        help_text=texts.HELP_CHOISE_COLOR
    )
    slug = models.SlugField('URL', unique=True,
                            validators=[validators.validate_slug],)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


def get_upload_path(instance, filename):
    model = instance._meta
    name = model.default_related_name.replace(' ', '_')
    return f'{name}/images/{filename}'


class Product(models.Model):
    """Абстрактная модель товара."""

    name = models.CharField('Наименовение',
                            max_length=Limits.MAX_LEN_TAG.value,)
    image = models.ImageField('Изображение', upload_to=get_upload_path,)
    description = models.TextField('Описание')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ReviewAndCommentModel(models.Model):
    """Абстрактная модель. Добавляет текст, автора и дату публикации."""

    text = models.CharField(
        'Текст',
        max_length=Limits.LENG_MAX_REVIEW.value,
        help_text='Введите текст'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    class Meta:
        abstract = True
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:Limits.LENG_CUT.value]


class Period(models.Model):
    """Модель периода аренды."""

    name = models.CharField(
        'Название',
        help_text='Укажите название периода',
        max_length=Limits.MAX_LEN_TAG.value,
        blank=False,
        unique=True,
    )

    value = models.PositiveSmallIntegerField(
        'Количество дней',
        help_text='Задайте количество дней',
    )

    class Meta:
        verbose_name = 'Период аренды'
        verbose_name_plural = 'Периоды аренды'
        ordering = ('name',)
        constraints = [
            models.UniqueConstraint(fields=['name', 'value'],
                                    name='unique_period')
        ]

    def __str__(self):
        return self.name


class Feedback(models.Model):
    """Модель обратной связи."""

    user = models.ForeignKey(User, verbose_name='Пользователь',
                             on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('Имя', max_length=Limits.MAX_NAME.value,
                            help_text='Введите ваше имя',
                            validators=[validate_not_empty])
    email = models.EmailField('Электронный адрес (email)', 
                              help_text='Оставьте своё сообщение',
                              validators=[validate_not_empty])
    subject = models.CharField('Тема письма',
                               max_length=Limits.MAX_LENGTH.value)
    content = models.TextField('Содержимое письма',
                               validators=[validate_not_empty])
    time_create = models.DateTimeField('Дата отправки', auto_now_add=True)
    ip_address = models.GenericIPAddressField(verbose_name='IP отправителя', 
                                              blank=True, null=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-time_create']

    def __str__(self):
        return f'Вам письмо от {self.email}'
