# Generated by Django 4.1.7 on 2023-04-25 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'default_related_name': 'genres', 'ordering': ('-name',), 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
    ]
