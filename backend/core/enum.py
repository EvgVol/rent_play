from enum import Enum, IntEnum


class Limits(IntEnum):
    # Максимальная длина email (User)
    MAX_LEN_EMAIL_FIELD = 256
    # Максимальная длина строковых полей моделей в приложении "users"
    MAX_LEN_USERS_CHARFIELD = 32
    # Минимальная длина юзернейма (User)
    MIN_LEN_USERNAME = 3
