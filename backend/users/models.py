from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from core import texts, validators
from core.enum import Limits


class User(AbstractUser):
    """Модель пользователя."""

    USER = 'user'
    RENTOR = 'rentor'

    ROLE_CHOICES = [
        (USER, 'Пользователь'),
        (RENTOR, 'Арендодатель'),
    ]

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
        max_length=Limits.MAX_LEN_ROLE.value,
        choices=ROLE_CHOICES,
        default=USER,
        blank=True
    )

    birthdate = models.DateField(
        'Дата рождения',
        blank=True,
        null=True,
    )

    avatar = models.ImageField('Аватар', help_text=texts.USER_AVATAR,)
    phone_number = PhoneNumberField(blank=False, null=False, region="RU")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'role', 'first_name',
                       'last_name', 'phone_number')

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

    def __str__(self):
        return f'{self.username}: {self.email}'


class Follow(models.Model):
    """Модель подписчика."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Арендатель',
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Арендодатель',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('user',)
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_follow'
            ),
            models.CheckConstraint(
                check=~models.Q(author=models.F('user')),
                name='no_self_follow'
            )
        ]

    def __str__(self):
        return f'Пользователь {self.user} подписан на {self.author}'
