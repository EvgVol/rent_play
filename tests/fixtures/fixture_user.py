import pytest


@pytest.fixture
def user_1(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser1',
        password='TestPassword1',
        email='test1@example.com',
        first_name='TestUser1',
        last_name='TestUser1',
        role='rentor',
        birthdate='2000-01-01',
        avatar=None,
    )


@pytest.fixture
def user_2(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser2',
        password='TestPassword2',
        email='test2@example.com',
        first_name='TestUser2',
        last_name='TestUser2',
        role='user',
        birthdate='2000-01-02',
        avatar=None,
    )


@pytest.fixture
def user_3(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser3',
        password='TestPassword3',
        email='test3@example.com',
        first_name='TestUser3',
        last_name='TestUser3',
        role='user',
        birthdate='2000-01-03',
        avatar=None,
    )


@pytest.fixture
def user_4(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser4',
        password='TestPassword4',
        email='test4@example.com',
        first_name='TestUser4',
        last_name='TestUser4',
        role='rentor',
        birthdate='2000-01-04',
        avatar=None,
    )


@pytest.fixture
def superuser(django_user_model):
    return django_user_model.objects.create_superuser(
        username='admin',
        password='TestPassword4',
        email='admin@example.com',
        first_name='TestAdmin-fn',
        last_name='TestAdmin_ln',
        role='user',
        birthdate='2000-01-05',
        avatar=None
    )
