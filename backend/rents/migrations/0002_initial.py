# Generated by Django 4.1.7 on 2023-03-31 05:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leaser', to=settings.AUTH_USER_MODEL, verbose_name='Арендатель'),
        ),
    ]
