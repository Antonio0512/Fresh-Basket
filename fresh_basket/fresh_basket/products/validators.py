from django.core.exceptions import ValidationError


def validate_positive_price(value):
    if value <= 0:
        raise ValidationError('Price must be a positive value.')


def validate_name_length(value):
    if len(value) < 2:
        raise ValidationError('Name length must be at least 2 characters.')


def validate_file_size(value):
    filesize = value.size
    if filesize > 8 * 1024 * 1024:
        raise ValidationError("The file size must be less than 8 MB!")
