from django.shortcuts import get_object_or_404

from fresh_basket.products.models import Product
from .models import UserView, UserCart, UserPurchase


def record_user_view(user, product):
    user_view_count = UserView.objects.filter(user=user).count()
    if user_view_count >= 20:
        oldest_user_view = UserView.objects.filter(user=user).order_by('timestamp').first()
        oldest_user_view.delete()

    if user.is_authenticated:
        UserView.objects.create(user=user, product=product)


def record_user_cart(user, product_id, quantity):
    product = get_object_or_404(Product, id=product_id)
    user_cart_count = UserCart.objects.filter(user=user).count()
    if user_cart_count >= 20:
        oldest_user_cart = UserCart.objects.filter(user=user).order_by('timestamp').first()
        oldest_user_cart.delete()

    if user.is_authenticated:
        UserCart.objects.create(user=user, product=product, quantity=quantity)


def record_user_purchase(user, product):
    user_purchase_count = UserPurchase.objects.filter(user=user).count()
    if user_purchase_count >= 10:
        oldest_user_purchase = UserPurchase.objects.filter(user=user).order_by('timestamp').first()
        oldest_user_purchase.delete()

    if user.is_authenticated:
        UserPurchase.objects.get_or_create(user=user, product=product)
