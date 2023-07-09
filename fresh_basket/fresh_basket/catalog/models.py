from django.db import models
from . import validators


class Catalog(models.Model):
    name = models.CharField(max_length=100,
                            blank=False,
                            null=False
                            )
    description = models.TextField(
        blank=False,
        null=False
    )

    catalog_image = models.ImageField(upload_to='catalog_pics',
                                      validators=[validators.validate_file_size],
                                      null=True,
                                      blank=True
                                      )

    def __str__(self):
        return self.name
