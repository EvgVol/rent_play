# Generated by Django 4.1.7 on 2023-03-22 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название периода', max_length=30, unique=True, verbose_name='Наименование периода')),
                ('value', models.CharField(help_text='Введите значение', max_length=30, unique=True, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Период',
                'verbose_name_plural': 'Периоды',
                'ordering': ('name',),
            },
        ),
        migrations.AddConstraint(
            model_name='timerent',
            constraint=models.UniqueConstraint(fields=('name', 'value'), name='unique_timerent'),
        ),
    ]