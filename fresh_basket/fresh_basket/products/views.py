from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Product
from .forms import DetailsAddToCartForm, ProductSearchForm
from ..recommendations.views import generate_recommendations
from ..user_history.views import record_user_view
from .tasks import send_sunday_email

class AllProductsListView(ListView):
    model = Product
    template_name = 'products/all_products.html'
    context_object_name = 'products'
    form_class = ProductSearchForm

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(description__icontains=search_query)
            )
        return queryset


class DiscountProductsListView(ListView):
    model = Product
    template_name = 'products/discount_products.html'
    context_object_name = 'products'
    form_class = ProductSearchForm

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(discount_catalog__isnull=False)

        search_query = self.request.GET.get('q')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(description__icontains=search_query)
            )

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
