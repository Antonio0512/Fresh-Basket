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


class ProductReviewsListView(ListView):
    model = models.Review
    template_name = 'common/reviews-list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        product_id = self.kwargs['pk']
        return models.Review.objects.filter(product_id=product_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_pk'] = self.kwargs['pk']
        return context


class AddReviewToProduct(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        review_content = request.POST.get('review-content')
        review_rating = request.POST.get('review-rating')

        if review_content:
            models.Review.objects.create(
                product=product,
                user=request.user,
                content=review_content,
                rating=review_rating
            )

        referring_url = request.META.get('HTTP_REFERER')
        return redirect(referring_url)
