import pytest
import json

from games.models import Tag, Game
from consoles.models import Category
from core.models import Period


@pytest.fixture
def tag_one():
    return Tag.objects.create(
        name='Single', color='#E26C2D', slug='single'
    )


@pytest.fixture
def tag_second():
    return Tag.objects.create(
        name='Double', color='#ffff00', slug='double'
    )


@pytest.fixture
def tag_third():
    return Tag.objects.create(
        name='Third', color='#ff0000', slug='third'
    )


@pytest.fixture
def category_1():
    return Category.objects.create(
        name='PS4 Slim', color='#003366', slug='slim'
    )


@pytest.fixture
def category_2():
    return Category.objects.create(
        name='PS4 PRO', color='#002137', slug='pro'
    )


@pytest.fixture
def game_single():
    return Game.objects.create(
        name="string1",
        description="string1",
        tags=[tag_one.id,],
        image=('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA'
               'EAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAA'
               'AACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAgg'
               'CByxOyYQAAAABJRU5ErkJggg=='),
    )


@pytest.fixture
def game_second():
    return Game.objects.create(
        name="string2",
        description="string2",
        tags=[tag_second.id,],
        image=('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA'
               'EAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAA'
               'AACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAgg'
               'CByxOyYQAAAABJRU5ErkJggg=='),
    )


@pytest.fixture
def day():
    return Period.objects.create(
        name='Сутки', value='1'
    )


@pytest.fixture
def three_days():
    return Period.objects.create(
        name='Трое суток', value='3'
    )


@pytest.fixture
def games():
    return ('/api/games/')
