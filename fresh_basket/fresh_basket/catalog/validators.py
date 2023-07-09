from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size
    if filesize > 5 * 1024 * 1024:
        raise ValidationError("The file size must be less than 5 MB!")
