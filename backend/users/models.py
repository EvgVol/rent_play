"""Модуль для создания, настройки и управления моделью пользователей.
Задаёт модели и методы для настроийки и управления пользователями
приложения `Rent_play`. Модель пользователя основана на модели
AbstractUser из Django для переопределения полей обязательных для заполнения.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser

from core.enums import Limits
from core import texts, validators


class User(AbstractUser):
    """Модель пользователя."""

    username = models.CharField(
        'Уникальный юзернейм',
        validators=(validators.validate_username,),
        max_length=Limits.MAX_LEN_USERS_CHARFIELD.value,
        unique=True,
        blank=True,
        help_text=texts.USERS_HELP_UNAME,
        error_messages={'unique': texts.UNIQUE_USERNAME},
    )

    first_name = models.CharField(
        'Имя',
        max_length=Limits.MAX_LEN_USERS_CHARFIELD.value,
        blank=True,
        help_text=texts.USERS_HELP_FNAME,
    )

    last_name = models.CharField(
        'Фамилия',
        max_length=Limits.MAX_LEN_USERS_CHARFIELD.value,
        blank=True,
        help_text=texts.USERS_HELP_FNAME,
    )

    email = models.EmailField(
        'Электронная почта',
        max_length=Limits.MAX_LEN_EMAIL_FIELD.value,
        unique=True,
        blank=True,
        help_text=texts.USERS_HELP_EMAIL
    )
    

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}: {self.email}'
