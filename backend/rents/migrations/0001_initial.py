# Generated by Django 4.1.7 on 2023-03-26 11:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
        ('consoles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameInRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Время аренды не может быть меньше 1 дня!')], verbose_name='Время аренды в днях')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('console', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_item', to='consoles.console', verbose_name='Приставка')),
                ('games', models.ManyToManyField(through='rents.GameInRent', to='games.game', verbose_name='Игры')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': [models.OrderBy(models.F('user'), nulls_last=True)],
            },
        ),
    ]
