# Generated by Django 4.1.7 on 2023-04-25 04:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='end_date',
            field=models.DateField(default=datetime.date(2023, 4, 26), help_text='Укажите дату окончание аренды', verbose_name='Конец аренды'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='start_date',
            field=models.DateField(default=datetime.date(2023, 4, 25), help_text='Укажите дату начала аренды', verbose_name='Начало аренды'),
        ),
    ]
