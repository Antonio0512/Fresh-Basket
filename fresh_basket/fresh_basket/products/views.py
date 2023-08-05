from django.views.generic import ListView, DetailView
from .models import Product
from .forms import DetailsAddToCartForm
from ..recommendations.views import generate_recommendations
from ..user_history.views import record_user_view


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
        queryset = queryset.filter(discount_catalog__isnull=False)
        return queryset


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'products/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DetailsAddToCartForm()
        user = self.request.user
        product = self.get_object()

        if user.is_authenticated:
            record_user_view(user, product)

        generate_recommendations(user)

        return context
