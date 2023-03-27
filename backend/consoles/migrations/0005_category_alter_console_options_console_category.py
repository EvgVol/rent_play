# Generated by Django 4.1.7 on 2023-03-27 06:50

import colorfield.fields
import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('consoles', '0004_remove_console_album_imagesinconsole_console_images_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ограничение 50 символов!', max_length=50, unique=True, verbose_name='Наименовение')),
                ('color', colorfield.fields.ColorField(default='#FF0000', error_messages={'unique': 'Такой цвет уже существует!'}, help_text='Для выбора цвета воспользуйтесь цветовой панелью.', image_field=None, max_length=7, samples=None, unique=True, validators=[django.core.validators.RegexValidator(message='Введенное значение не является цветом в формате HEX', regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')], verbose_name='Цветовой HEX-код')),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'abstract': False,
                'default_related_name': 'categories',
            },
        ),
        migrations.AlterModelOptions(
            name='console',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Игровая приставка', 'verbose_name_plural': 'Игровые приставки'},
        ),
        migrations.AddField(
            model_name='console',
            name='category',
            field=models.ManyToManyField(to='consoles.category', verbose_name='Категории'),
        ),
    ]
