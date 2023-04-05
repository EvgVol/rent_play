import re

from django.core.exceptions import ValidationError

from core.enum import Regex
from core.texts import NOT_ALLOWED_CHAR_MSG, NOT_ALLOWED_ME


def validate_username(username):
    """Валидация имени пользователя."""
    invalid_symbols = ''.join(
        set(re.sub(Regex.USERNAME_REGEX, '', username))
    )
    if invalid_symbols:
        raise ValidationError(
            NOT_ALLOWED_CHAR_MSG.format(
                chars=invalid_symbols, username=username))
    if username == 'me':
        raise ValidationError(
            NOT_ALLOWED_ME.format(username=username)
        )
    return username
