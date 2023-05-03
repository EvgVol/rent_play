# Generated by Django 4.1.7 on 2023-05-03 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0005_alter_rent_end_date_alter_rent_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='end_date',
            field=models.DateField(default=datetime.date(2023, 5, 4), help_text='Укажите дату окончание аренды', verbose_name='Конец аренды'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='start_date',
            field=models.DateField(default=datetime.date(2023, 5, 3), help_text='Укажите дату начала аренды', verbose_name='Начало аренды'),
        ),
    ]
