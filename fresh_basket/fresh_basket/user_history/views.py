from django.shortcuts import get_object_or_404

from fresh_basket.products.models import Product
from .models import UserView, UserCart, UserPurchase


def record_user_view(user, product):
    UserView.objects.create(user=user, product=product)


def record_user_cart(user, product_id, quantity):
    product = get_object_or_404(Product, id=product_id)

    if user.is_authenticated:
        UserCart.objects.create(user=user, product=product, quantity=quantity)


def record_user_purchase(user, product):
    UserPurchase.objects.get_or_create(user=user, product=product)
