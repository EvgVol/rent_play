import csv
import os

from django.conf import settings

from consoles.models import Category
from games.models import Tag

FILE_DIR = os.path.join(settings.BASE_DIR, 'data')


def import_csv():
    """Импортер данных из csv."""
    with open(
        os.path.join(FILE_DIR, 'categories.csv'), 'r', encoding='utf-8'
    ) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name, color, slug = row
            Category.objects.get_or_create(name=name,
                                           color=color,
                                           slug=slug)
        print(f'Файл {csvfile.name} загружен.')

    with open(
        os.path.join(FILE_DIR, 'tags.csv'), 'r', encoding='utf-8'
    ) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name, color, slug = row
            Tag.objects.get_or_create(name=name,
                                      color=color,
                                      slug=slug)
        print(f'Файл {csvfile.name} загружен.')
