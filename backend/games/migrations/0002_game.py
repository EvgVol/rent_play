# Generated by Django 4.1.7 on 2023-03-21 10:01

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименовение')),
                ('image', models.ImageField(blank=True, null=True, upload_to='games/', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='URL')),
                ('tags', models.ManyToManyField(to='games.tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
    ]
