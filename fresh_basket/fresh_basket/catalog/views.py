from django.views.generic import TemplateView
from .models import Catalog


class CatalogView(TemplateView):
    template_name = 'catalog/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_catalogs'] = Catalog.objects.filter(name='All Products Catalog')[0]
        context['discounted_catalogs'] = Catalog.objects.filter(name='Discount Catalog')[0]
        return context
