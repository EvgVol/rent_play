# Generated by Django 4.1.7 on 2023-08-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_last_seen_remove_user_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(help_text='Наличие аватара увеличивает к вам доверие', upload_to='users/images/', verbose_name='Аватар'),
        ),
    ]