from django.db import models
from django.core import validators
from colorfield.fields import ColorField

from core import texts
from core.enum import Limits, Regex


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
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'


class Image(models.Model):
    """Абстрактная модель изображений."""

    name = models.CharField(max_length=255, blank=False)
    image = models.ImageField('Изображение', upload_to=get_upload_path, blank=False)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'image'],
                name='unique_name_image',
            )
        ]


