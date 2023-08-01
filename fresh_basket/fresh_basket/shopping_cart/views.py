from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CartItem
from ..products.models import Product
from .forms import AddToCartForms


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
        form = AddToCartForms(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')
            weight = form.cleaned_data.get('weight')
            if quantity is not None and weight is None:
                try:
                    cart_item = CartItem.objects.get(user=request.user, product=product)
                    cart_item.quantity = quantity if cart_item.quantity is None else cart_item.quantity + quantity
                    # cart_item.weight = weight if cart_item.weight and cart_item.weight is None else cart_item.weight + weight
                    cart_item.save()
                    messages.success(request, 'Product added to cart successfully.')
                except CartItem.DoesNotExist:
                    CartItem.objects.create(user=request.user, product=product, quantity=quantity, weight=weight)

            if weight is not None and quantity is None:
                try:
                    cart_item = CartItem.objects.get(user=request.user, product=product)
                    # cart_item.quantity = quantity if cart_item.quantity is None else cart_item.quantity + quantity
                    cart_item.weight = weight if cart_item.weight and cart_item.weight is None else cart_item.weight + weight
                    cart_item.save()
                    messages.success(request, 'Product added to cart successfully.')
                except CartItem.DoesNotExist:
                    CartItem.objects.create(user=request.user, product=product, quantity=quantity, weight=weight)

            if weight is None and quantity is None:
                messages.error(request,
                               'You try to enter empty qty or weight. Please enter a valid number')

        else:
            messages.error(request, 'You entered invalid data, please try again')

        return redirect('all-product-details', pk=pk)


class DeleteFromCartView(LoginRequiredMixin, DeleteView):
    model = CartItem
    success_url = reverse_lazy('shopping-cart')

    def form_valid(self, form):
        messages.success(self.request, "Item successfully removed from the cart.")
        return super().form_valid(form)
