from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView, FormView

from .forms import ReviewForm
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


class ProductReviewsListView(ListView):
    model = models.Review
    template_name = 'common/reviews-list.html'
    context_object_name = 'reviews'
    form_class = ReviewForm

    def get_queryset(self):
        product_id = self.kwargs.get('pk')
        return models.Review.objects.filter(product_id=product_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_pk'] = self.kwargs.get('pk')
        context['form'] = self.form_class()  # Pass the form instance to the template
        return context


class AddReviewToProduct(LoginRequiredMixin, FormView):
    template_name = 'common/reviews-list.html'
    form_class = ReviewForm

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse_lazy('product-reviews', kwargs={'pk': pk})

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        review = form.save(commit=False)
        review.product = product
        review.user = self.request.user
        review.save()

        messages.success(self.request, 'Review added successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please enter review content and rating.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_pk'] = self.kwargs['pk']
        return context
