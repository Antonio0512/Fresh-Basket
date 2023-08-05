from collections import Counter

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Recommendation
from ..products.models import Product
from ..user_history.models import UserView

User = get_user_model()


def generate_recommendations(user):
    products_viewed_by_user = UserView.objects.filter(user=user).values_list('product', flat=True)
    product_id_counts = Counter(products_viewed_by_user)

    recommended_products = [product_id for product_id, _ in product_id_counts.most_common(5)]

    Recommendation.objects.filter(user=user).delete()
    for product_id in recommended_products:
        product = Product.objects.get(pk=product_id)
        Recommendation.objects.create(user=user, product=product)
