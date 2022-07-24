import re

from django.core.exceptions import ValidationError


def only_letters_validator(value):
    regex = r"[a-zA-Z]+"
    matches = re.findall(regex, value)
    if not matches:
        raise ValidationError('Please use only letters')
