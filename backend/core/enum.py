from enum import Enum, IntEnum


class Limits(IntEnum):
    # Максимальная длина email (User)
    MAX_LEN_EMAIL_FIELD = 256
    # Максимальная длина строковых полей моделей в приложении "users"
    MAX_LEN_USERS_CHARFIELD = 32
    # Минимальная длина юзернейма (User)
    MIN_LEN_USERNAME = 3
    # Максимальная длина тега
    MAX_LEN_TAG = 50
    # Максимальная длина цвета
    LENG_COLOR = 7

class Regex:
    # Регулярное выражение для цвета тэга
    COLOR_REGEX = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
