from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView

from . import models
from fresh_basket.products.models import Product
from fresh_basket.promotions.models import Promotions


def home(request):
    promotions = Promotions.objects.all()

    context = {
        'promotions': promotions
    }
    return render(request, 'common/home.html', context)


class AddToFavoritesView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if models.Favourite.objects.filter(user=request.user, product=product).exists():
            messages.error(request, 'This product is already in your favorites.')

        else:
            models.Favourite.objects.create(user=request.user, product=product)
            messages.success(request, 'Product added to favorites successfully.')

        referring_url = request.META.get('HTTP_REFERER')

        return redirect(referring_url)


class FavoriteListView(LoginRequiredMixin, ListView):
    model = models.Favourite
    template_name = 'favourites/favourites-list.html'
    context_object_name = 'favourites'

    def get_queryset(self):
        return models.Favourite.objects.filter(user=self.request.user)


class RemoveFromFavouritesView(LoginRequiredMixin, DeleteView):
    model = models.Favourite
    template_name = 'favourites/favourites-list.html'  # Replace with your template name
    success_url = reverse_lazy('favourites-products')  # Replace with your favorites URL

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Product removed from favorites successfully.')
        return super().delete(request, *args, **kwargs)
