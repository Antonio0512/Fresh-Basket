from django.core.exceptions import ValidationError


def validate_positive_price(value):
    if value <= 0:
        raise ValidationError('Price must be a positive value.')


def validate_name_length(value):
    if len(value) < 2:
        raise ValidationError('Name length must be at least 2 characters.')
