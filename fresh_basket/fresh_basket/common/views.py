from django.shortcuts import render
from django.views.generic import TemplateView

from fresh_basket.recommendations.models import Recommendation


class HomeView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            recommended_products = Recommendation.objects.filter(user=self.request.user)
            context['recommended_products'] = recommended_products

        return context