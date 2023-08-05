from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView

from fresh_basket.favorites import models
from fresh_basket.products.models import Product


class AddToFavoritesView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            product = get_object_or_404(Product, pk=pk)
            if models.Favourite.objects.filter(user=request.user, product=product).exists():
                messages.error(request, 'This product is already in your favorites.')

            else:
                models.Favourite.objects.create(user=request.user, product=product)
                messages.success(request, 'Product added to favorites successfully.')
        except ObjectDoesNotExist:
            messages.error(request, 'Product not found.')

        return redirect('favourite-products-details', pk=pk)


class FavoriteListView(LoginRequiredMixin, ListView):
    model = models.Favourite
    template_name = 'common/favourites-list.html'
    context_object_name = 'favourites'

    def get_queryset(self):
        return models.Favourite.objects.filter(user=self.request.user)


class RemoveFromFavouritesView(LoginRequiredMixin, DeleteView):
    model = models.Favourite
    template_name = 'common/favourites-list.html'
    success_url = reverse_lazy('favourites-products')

    def form_valid(self, form):
        messages.success(self.request, 'Product removed from favorites successfully.')
        return super().form_valid(form)
