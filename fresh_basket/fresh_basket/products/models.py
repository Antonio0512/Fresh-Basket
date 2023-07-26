from django.db import models

from fresh_basket.catalog.models import Catalog
from fresh_basket.products import validators


class Product(models.Model):
    name = models.CharField(max_length=100,
                            null=False,
                            blank=False,
                            validators=[validators.validate_name_length]
                            )
    description = models.TextField(null=False,
                                   blank=False
                                   )
    price = models.DecimalField(max_digits=8,
                                decimal_places=2,
                                validators=[validators.validate_positive_price]
                                )
    old_price = models.DecimalField(max_digits=8,
                                    decimal_places=2,
                                    null=True, blank=True
                                    )

    image = models.ImageField(upload_to='product_pics/',
                              validators=[validators.validate_file_size],
                              blank=True,
                              null=True
                              )

    has_weight = models.BooleanField(default=False)

    catalog = models.ForeignKey(Catalog,
                                on_delete=models.CASCADE,
                                null=True, blank=True,
                                related_name='products'
                                )
    discount_catalog = models.ForeignKey(Catalog,
                                         on_delete=models.CASCADE,
                                         null=True, blank=True,
                                         related_name='discounts'
                                         )

    def __str__(self):
        return self.name
