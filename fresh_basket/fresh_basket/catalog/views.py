from django.views.generic import TemplateView
from .models import Catalog


class CatalogView(TemplateView):
    template_name = 'catalog/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_catalogs = Catalog.objects.filter(name='All Products Catalog')
        discounted_catalogs = Catalog.objects.filter(name='Discount Catalog')

        if all_catalogs.exists():
            context['all_catalogs'] = all_catalogs[0]
        else:
            context['all_catalogs'] = None

        if discounted_catalogs.exists():
            context['discounted_catalogs'] = discounted_catalogs[0]
        else:
            context['discounted_catalogs'] = None

        return context
