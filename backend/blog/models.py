from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class CreatedModel(models.Model):
    """Абстрактная модель. Добавляет дату создания и дату."""

    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    class Meta:
        abstract = True
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        return self.text[:15]


class Group(models.Model):
    """Параметры добавления новых групп."""

    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('URL', unique=True,)
    description = models.TextField('Описание')

    class Meta:
        """Сортировка по названию."""

        ordering = ('-title',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        return self.title


class Post(CreatedModel):
    """Параметры добавления новых постов."""

    text = models.TextField(
        'Текст',
        help_text='Введите текст поста'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа',
        help_text='Группа, к которой будет относиться пост'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        blank=True
    )

    class Meta:
        """Сортировка по дате убывания."""

        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        default_related_name = 'posts'
