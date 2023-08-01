from django.db import models

from django.contrib.auth import get_user_model

from fresh_basket.products.models import Product

User = get_user_model()


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, null=True)
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    @property
    def has_weight(self):
        return self.product.has_weight

    def subtotal(self):
        if self.has_weight:
            return round(self.weight * self.product.price, 2)
        else:
            return round(self.quantity * self.product.price, 2)
