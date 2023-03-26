# Generated by Django 4.1.7 on 2023-03-26 18:12

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consoles', '0004_remove_console_album_imagesinconsole_console_images_and_more'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.RemoveField(
            model_name='image',
            name='album',
        ),
        migrations.RemoveField(
            model_name='image',
            name='default',
        ),
        migrations.RemoveField(
            model_name='image',
            name='length',
        ),
        migrations.RemoveField(
            model_name='image',
            name='width',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=core.models.get_upload_path, verbose_name='Изображение'),
        ),
        migrations.AddConstraint(
            model_name='image',
            constraint=models.UniqueConstraint(fields=('name', 'image'), name='unique_name_image'),
        ),
        migrations.DeleteModel(
            name='ImageAlbum',
        ),
    ]
