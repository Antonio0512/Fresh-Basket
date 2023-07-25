from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)

    status = models.CharField(max_length=20)

    card_number = models.CharField(max_length=16)
    card_holder_name = models.CharField(max_length=100)
    expiration_month = models.PositiveSmallIntegerField()
    expiration_year = models.PositiveSmallIntegerField()
    cvv = models.CharField(max_length=4)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

