from django.views.generic import ListView

from .models import Promotions


class AllPromotionsListView(ListView):
    model = Promotions
    template_name = 'promotions/all-promotions.html'
    context_object_name = 'promotions'