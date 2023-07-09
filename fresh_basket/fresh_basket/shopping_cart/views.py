from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, View
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
        context['cart_total'] = sum(item.subtotal() for item in CartItem.objects.all())
        return context


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        quantity = int(request.POST.get('quantity', 1))

        try:
            cart_item = CartItem.objects.get(user=request.user, product=product)
            cart_item.quantity += quantity
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(user=request.user, product=product, quantity=quantity)
            cart_item.save()

        return redirect('product-details', product.pk)


class DeleteFromCartView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        item = CartItem.objects.filter(user=request.user, pk=product_id).first()
        if item:
            item.delete()
            messages.success(request, "Item successfully removed from the cart.")
        else:
            messages.error(request, "Failed to delete item from the cart.")
        return redirect('shopping-cart')
