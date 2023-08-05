from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, FormView

from fresh_basket.products.models import Product
from fresh_basket.reviews import models
from fresh_basket.reviews.forms import ReviewForm


class ProductReviewsListView(ListView):
    model = models.Review
    template_name = 'reviews/reviews-list.html'
    context_object_name = 'reviews'
    form_class = ReviewForm

    def get_queryset(self):
        product_id = self.kwargs.get('pk')
        return models.Review.objects.filter(product_id=product_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_pk'] = self.kwargs.get('pk')
        context['form'] = self.form_class()
        return context


class AddReviewToProduct(LoginRequiredMixin, FormView):
    template_name = 'common/../../templates/reviews/reviews-list.html'
    form_class = ReviewForm

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse('product-reviews', kwargs={'pk': pk})

    def form_valid(self, form):
        try:
            product = get_object_or_404(Product, pk=self.kwargs['pk'])
            review = form.save(commit=False)
            review.product = product
            review.user = self.request.user
            review.save()
            messages.success(self.request, 'Review added successfully.')
            return super().form_valid(form)
        except ObjectDoesNotExist:
            messages.error(self.request, "Product not found")
            return redirect(reverse('product-reviews', kwargs={'pk': self.kwargs['pk']}))
        except ValidationError:
            messages.error(self.request, 'Please enter valid content and rating.')
            return redirect(reverse('product-reviews', kwargs={'pk': self.kwargs['pk']}))

    def form_invalid(self, form):
        messages.error(self.request, 'Please enter valid content and rating.')
        pk = self.kwargs.get('pk')
        return redirect(reverse('product-reviews', kwargs={'pk': pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_pk'] = self.kwargs['pk']
        return context
