import csv
import os

from consoles.models import Console
from django.conf import settings
from games.models import Tag

FILE_DIR = os.path.join(settings.BASE_DIR, 'data')


def import_csv():
    """Импортер данных из csv."""
    with open(
        os.path.join(FILE_DIR, 'categoies.csv'), 'r', encoding='utf-8'
    ) as csvfile:
        reader_categoies = csv.reader(csvfile)
        for row in reader_categoies:
            name, color, slug = row
            Console.objects.get_or_create(name=name,
                                          color=color,
                                          slug=slug)
        print(f'Файл {csvfile.name} загружен.')

    with open(
        os.path.join(FILE_DIR, 'tags.csv'), 'r', encoding='utf-8'
    ) as csvfile:
        reader_tags = csv.reader(csvfile)
        for row in reader_tags:
            name, color, slug = row
            Tag.objects.get_or_create(name=name,
                                      color=color,
                                      slug=slug)
        print(f'Файл {csvfile.name} загружен.')
