from django.db import models


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
                                      null=True,
                                      blank=True
                                      )

    def __str__(self):
        return self.name
