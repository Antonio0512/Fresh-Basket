from django.views.generic import ListView

from .models import Promotion


class AllPromotionsListView(ListView):
    model = Promotion
    template_name = 'promotions/all-promotions.html'
    context_object_name = 'promotions'