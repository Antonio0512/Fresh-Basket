import decimal
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CartItem
from ..products.models import Product


class ShoppingCartView(LoginRequiredMixin, ListView):
    model = CartItem
    template_name = 'shopping cart/shopping_cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_total'] = sum(item.subtotal() for item in CartItem.objects.filter(user=self.request.user))
        return context


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        quantity = int(request.POST.get('quantity', 1))
        weight = decimal.Decimal(request.POST.get('weight', 0.0))

        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product,
                                                            defaults={'quantity': quantity})

        cart_item.quantity += quantity
        cart_item.weight = weight if cart_item.weight is None else cart_item.weight + weight
        cart_item.save()

        return redirect(reverse('all-product-details', kwargs={'pk': pk}))


class DeleteFromCartView(LoginRequiredMixin, DeleteView):
    model = CartItem
    success_url = reverse_lazy('shopping-cart')

    def form_valid(self, form):
        messages.success(self.request, "Item successfully removed from the cart.")
        return super().form_valid(form)
