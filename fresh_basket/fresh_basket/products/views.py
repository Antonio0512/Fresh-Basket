from django.views.generic import ListView, DetailView
from .models import Product


class AllProductsListView(ListView):
    model = Product
    template_name = 'products/all_products.html'
    context_object_name = 'products'
    # paginate_by = 10


class DiscountProductsListView(ListView):
    model = Product
    template_name = 'products/discount_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter the products to display only the ones with discounts
        queryset = queryset.filter(discount_catalog__isnull=False)
        return queryset


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'products/product_details.html'
    context_object_name = 'product'
