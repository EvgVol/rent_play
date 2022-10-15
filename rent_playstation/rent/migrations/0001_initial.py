# Generated by Django 3.2 on 2022-10-15 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='rent/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Приставка',
                'verbose_name_plural': 'Приставки',
            },
        ),
        migrations.CreateModel(
            name='RentalRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=50, verbose_name='Срок аренды')),
                ('cost', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('console', models.ForeignKey(blank=True, help_text='Выберите приставку', null=True, on_delete=django.db.models.deletion.SET_NULL, to='rent.console', verbose_name='Приставка')),
                ('period', models.ForeignKey(blank=True, help_text='Укажите срок аренды', null=True, on_delete=django.db.models.deletion.SET_NULL, to='rent.rentalrate', verbose_name='Срок аренды')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
