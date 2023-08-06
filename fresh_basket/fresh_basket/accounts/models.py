from django.contrib.auth.models import AbstractUser
from django.db import models

from . import validators


class MarketUser(AbstractUser):

    username = models.CharField(
        unique=True,
        max_length=30,
        validators=[validators.validate_min_username_length]
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False
    )

    first_name = models.CharField(
        max_length=30,
        validators=[validators.validate_min_name_length, validators.validate_only_letters]
    )

    last_name = models.CharField(
        max_length=30,
        validators=[validators.validate_min_name_length, validators.validate_only_letters]
    )

    profile_picture = models.ImageField(
        upload_to='profile_pics/'
    )

    gender = models.CharField(
        max_length=30,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Do not show', 'Do not show')
        )
    )
