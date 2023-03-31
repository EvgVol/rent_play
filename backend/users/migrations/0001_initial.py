# Generated by Django 4.1.7 on 2023-03-31 05:38

import core.validators
import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(error_messages={'unique': 'Пользователь с таким именем уже существует!'}, help_text='Обязательно для заполнения. От 3 до 32 букв.', max_length=32, unique=True, validators=[core.validators.validate_username], verbose_name='Уникальный юзернейм')),
                ('first_name', models.CharField(help_text='Обязательно для заполнения. Максимум 32 букв.', max_length=32, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Обязательно для заполнения. Максимум 32 букв.', max_length=32, verbose_name='Фамилия')),
                ('email', models.EmailField(help_text='Обязательно для заполнения. Максимум 256 букв.', max_length=256, unique=True, verbose_name='Электронная почта')),
                ('role', models.CharField(blank=True, choices=[('user', 'Пользователь'), ('rentor', 'Арендодатель')], default='user', max_length=30, verbose_name='Роль')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('avatar', models.ImageField(help_text='Наличие аватара увеличивает к вам доверие', upload_to='', verbose_name='Аватар')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('username',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('username', 'email'), name='unique_username_email'),
        ),
    ]
