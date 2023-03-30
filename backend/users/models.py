"""Модуль для создания, настройки и управления моделью пользователей.
Задаёт модели и методы для настроийки и управления пользователями
приложения `Rent_play`. Модель пользователя основана на модели
AbstractUser из Django для переопределения полей обязательных для заполнения.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser

from core.enum import Limits
from core import texts, validators


class User(AbstractUser):
    """Модель пользователя."""

    USER = 'user'
    RENTOR = 'rentor'
    ADMIN = 'admin'
    MODERATOR = 'moderator'

    ROLE_CHOICES = (
        (USER, 'user'),
        (RENTOR, 'rentor'),
    )

    username = models.CharField(
        'Уникальный юзернейм',
        validators=(validators.validate_username,),
        max_length=Limits.MAX_LEN_USERS_CHARFIELD.value,
        unique=True,
        blank=False,
        null=False,
        help_text=texts.USERS_HELP_UNAME,
        error_messages={'unique': texts.UNIQUE_USERNAME},
    )

    first_name = models.CharField(
        'Имя',
        max_length=Limits.MAX_LEN_USERS_CHARFIELD.value,
        blank=False,
        null=False,
        help_text=texts.USERS_HELP_FNAME,
    )

    last_name = models.CharField(
        'Фамилия',
        max_length=Limits.MAX_LEN_USERS_CHARFIELD.value,
        blank=False,
        null=False,
        help_text=texts.USERS_HELP_FNAME,
    )

    email = models.EmailField(
        'Электронная почта',
        max_length=Limits.MAX_LEN_EMAIL_FIELD.value,
        unique=True,
        blank=False,
        null=False,
        help_text=texts.USERS_HELP_EMAIL
    )

    role = models.CharField(
        'Роль',
        max_length=max(len(role) for role, _ in ROLE_CHOICES),
        choices=ROLE_CHOICES,
        default=USER,
    )

    birthdate = models.DateField(
        'Дата рождения',
        blank=True,
        null=True,
    )

    avatar = models.ImageField('Аватар', help_text=texts.USER_AVATAR,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name',)

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email',
            )
        ]

    @property
    def is_rentor(self):
        return self.role == self.RENTOR

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    def __str__(self):
        return f'{self.username}: {self.email}'
