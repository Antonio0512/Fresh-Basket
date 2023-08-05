from django.db import models
from fresh_basket.products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
