import re

from django.core.exceptions import ValidationError


def validate_min_name_length(value):
    if len(value) < 2:
        raise ValidationError("Name must have at least 2 characters!")


def validate_only_letters(value):
    pattern = r'^[a-zA-Z]+$'
    if not re.match(pattern, value):
        raise ValidationError("Name must contain only letters (upper and lower case)!")


def validate_file_size(value):
    filesize = value.size
    if filesize > 6 * 1024 * 1024:
        raise ValidationError("The file size must be less than 6 MB!")


def validate_min_username_length(value):
    if len(value) < 2:
        raise ValidationError("Name must have at least 2 characters!")