from django.core.exceptions import ValidationError


def validate_not_empty(value):
    if value == '':
        raise ValidationError(
            'Параметр является обязательным',
            params={'value': value},
        )
