from django.core.validators import MinLengthValidator
from django.db import models

from to_do_app.commons.validators import only_letters_validator, file_max_size_in_mb_validator


class AuditEntity(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modify_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(AuditEntity):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH,
                                  validators=(MinLengthValidator(FIRST_NAME_MIN_LENGTH), only_letters_validator))
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH,
                                 validators=(MinLengthValidator(LAST_NAME_MIN_LENGTH), only_letters_validator))
    email = models.EmailField(null=True, blank=True)
    picture = models.ImageField(upload_to='static/image/profile', validators=(file_max_size_in_mb_validator,))
    day_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=max(len(x) for x, _ in GENDERS), choices=GENDERS, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'profile'
