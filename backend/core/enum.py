from enum import IntEnum


class Limits(IntEnum):
    # Максимальная длина email (User)
    MAX_LEN_EMAIL_FIELD = 256
    # Максимальная длина строковых полей моделей в приложении "users"
    MAX_LEN_USERS_CHARFIELD = 32
    # Максимальная длина навазвание роли
    MAX_LEN_ROLE = 30
    # Минимальная длина юзернейма (User)
    MIN_LEN_USERNAME = 3
    # Максимальная длина тега
    MAX_LEN_TAG = 50
    # Максимальная длина цвета
    LENG_COLOR = 7
    # Максимальная длина отзыва
    LENG_MAX_REVIEW = 256
    # Ограничение длины отзыва в админке.
    LENG_CUT = 30
    # Минимальное время аренды
    TIME_MIN_AMOUNT = 1
    # Максимальная длина наименование категории
    LENG_CATEGORY = 100
    # Минимальная стоимость аренды
    MIN_RENT = 500


class Regex:
    # Регулярное выражение для цвета тэга
    COLOR_REGEX = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
    # Регулярное выражение для username
    USERNAME_REGEX = r'[\w\.@+-]+'
    # Словарь для сопостановления латинской и русской стандартных раскладок.
    INCORRECT_LAYOUT = str.maketrans(
        'qwertyuiop[]asdfghjkl;\'zxcvbnm,./',
        'йцукенгшщзхъфывапролджэячсмитьбю.'
    )
