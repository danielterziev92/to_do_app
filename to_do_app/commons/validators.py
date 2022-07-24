import re

from django.core.exceptions import ValidationError


def only_letters_validator(value):
    regex = r"[a-zA-Z]+"
    matches = re.findall(regex, value)
    if not matches:
        raise ValidationError('Please use only letters')


def file_max_size_in_mb_validator(max_size):
    def validator(value):
        filesize = value.file.size
        megabyte_limit = max_size
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    return validator
