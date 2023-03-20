from django.db import models
from django.core import validators
from colorfield.fields import ColorField

from core.enum import Limits, Regex
from core import texts


class Tag(models.Model):
    """Модель тегов к играми"""

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

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'

    def __str__(self):
        return self.name


class Game(models.Model):
    """Модель игр."""

    name = models.CharField('Наименовение',
                            max_length=Limits.MAX_LEN_TAG.value,)
    image = models.ImageField('Изображение', upload_to='rent/',
                              null=True, blank=True,)
    description = models.TextField('Описание')
    slug = models.SlugField('URL', unique=True,
                            validators=[validators.validate_slug],)
    tags = models.ForeignKey(verbose_name='Тег', blank=True,)

    class Meta:
        verbose_name_plural = 'Игры'
        verbose_name = 'Игра'

    def __str__(self):
        return self.name