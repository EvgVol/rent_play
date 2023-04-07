import pytest
import json

from games.models import Tag, Game
from consoles.models import Category, Console
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
