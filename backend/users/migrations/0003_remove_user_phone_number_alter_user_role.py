# Generated by Django 4.1.7 on 2023-03-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_avatar_user_birthdate_user_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('rentor', 'rentor')], default='user', max_length=6, verbose_name='Роль'),
        ),
    ]
