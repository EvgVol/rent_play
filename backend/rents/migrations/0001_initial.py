# Generated by Django 4.1.7 on 2023-03-30 07:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consoles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date(2023, 3, 30), help_text='Укажите дату начала аренды', verbose_name='Начало аренды')),
                ('end_date', models.DateField(default=datetime.date(2023, 3, 31), help_text='Укажите дату окончание аренды', verbose_name='Конец аренды')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('console', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_item', to='consoles.console', verbose_name='Приставка')),
            ],
            options={
                'verbose_name': 'Активный',
                'verbose_name_plural': 'Активные',
                'ordering': [models.OrderBy(models.F('user'), nulls_last=True)],
            },
        ),
    ]
