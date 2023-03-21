from .enum import Limits


"""help-texts for users.models"""
# help-text для email
USERS_HELP_EMAIL = (
    'Обязательно для заполнения. '
    f'Максимум {Limits.MAX_LEN_EMAIL_FIELD} букв.'
)
# help-text для username
USERS_HELP_UNAME = (
    'Обязательно для заполнения. '
    f'От {Limits.MIN_LEN_USERNAME} до {Limits.MAX_LEN_USERS_CHARFIELD} букв.'
)

# help-text для first_name/last_name
USERS_HELP_FNAME = (
    'Обязательно для заполнения. '
    f'Максимум {Limits.MAX_LEN_USERS_CHARFIELD} букв.'
)

NOT_ALLOWED_ME = (
    'Нельзя создать пользователя с '
    'именем: << {username} >> - это имя запрещено!'
)

NOT_ALLOWED_CHAR_MSG = (
    '{chars} недопустимые символы '
    'в имени пользователя {username}.'
)

UNIQUE_USERNAME = 'Пользователь с таким именем уже существует!'

WARNING_LIMIT_CHAR = f'Ограничение {Limits.MAX_LEN_TAG} символов!'

NOT_COLOR_HEX = 'Введенное значение не является цветом в формате HEX'

COLOR_NO_UNIQUE = 'Такой цвет уже существует!'

HELP_CHOISE_COLOR = 'Для выбора цвета воспользуйтесь цветовой панелью.'

TAG_ERROR = 'Рецепт не может быть без тегов!'

TAG_UNIQUE_ERROR = 'Теги должны быть уникальными!'

CONSOLE_IN_FAVORITE = 'Вы уже добавили рецепт в избранное.'

ALREADY_BUY = 'Вы уже добавили рецепт в список покупок.'