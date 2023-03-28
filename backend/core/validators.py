import re
import datetime

from django.core.exceptions import ValidationError
from rest_framework import status, serializers
from rest_framework.utils.representation import smart_repr


from core.texts import NOT_ALLOWED_CHAR_MSG, NOT_ALLOWED_ME


class DateValidator:
    """
    Validator for checking a start date and an end date field.
    Implementation based on `UniqueTogetherValidator` of Django Rest Framework.
    """
    message = 'Проверьте {start_date_field} и {end_date_field}.'

    def __init__(self, start_date_field="start_date", end_date_field="end_date", message=None):
        self.start_date_field = start_date_field
        self.end_date_field = end_date_field
        self.message = message or self.message

    def __call__(self, attrs):
        if (attrs[self.start_date_field] > attrs[self.end_date_field]
            or attrs[self.start_date_field] < datetime.date.today()
            or attrs[self.start_date_field] == attrs[self.end_date_field]):
            message = self.message.format(
                start_date_field=self.start_date_field,
                end_date_field=self.end_date_field,
            )
            raise serializers.ValidationError(message, code=status.HTTP_400_BAD_REQUEST)

    def __repr__(self):
        return '<%s(start_date_field=%s, end_date_field=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.start_date_field),
            smart_repr(self.end_date_field)
        )


def validate_username(username):
    """Валидация имени пользователя."""
    USERNAME_REGEX = r'[\w\.@+-]+'
    invalid_symbols = ''.join(
        set(re.sub(USERNAME_REGEX, '', username))
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
