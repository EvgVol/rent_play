# Generated by Django 4.1.7 on 2023-03-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consoles', '0007_rename_category_console_categories'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='console',
            name='unique_name_barcode',
        ),
        migrations.RemoveField(
            model_name='console',
            name='lessor',
        ),
        migrations.AddConstraint(
            model_name='console',
            constraint=models.UniqueConstraint(fields=('name', 'barcode'), name='unique_name_barcode'),
        ),
    ]