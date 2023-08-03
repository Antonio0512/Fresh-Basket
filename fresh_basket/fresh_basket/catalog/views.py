from django.views.generic import ListView
from .models import Catalog


class CatalogView(ListView):
    model = Catalog
    template_name = 'catalog/catalog.html'
    context_object_name = 'catalogs'

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
