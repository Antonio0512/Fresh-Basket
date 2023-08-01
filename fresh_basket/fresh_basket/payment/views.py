import stripe
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings
from stripe import error

from fresh_basket.shopping_cart.models import CartItem

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentView(TemplateView):
    template_name = "payments/payment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        cart_items = CartItem.objects.all()
        context['cart_items'] = cart_items

        line_items = []
        for cart_item in cart_items:
            if cart_item.has_weight:
                line_items.append({
                    'price': cart_item.product.stripe_price_id,
                    'quantity': int(cart_item.weight),
                })
            else:
                line_items.append({
                    'price': cart_item.product.stripe_price_id,
                    'quantity': cart_item.quantity,
                })

        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=self.request.build_absolute_uri('/payment/charge-success/'),
                cancel_url=self.request.build_absolute_uri('/payment/charge-cancel/')
            )
            context['CHECKOUT_SESSION_ID'] = session.id
            context['error_message'] = None
        except error.StripeError as e:
            context['CHECKOUT_SESSION_ID'] = None
            context['error_message'] = "An error occurred while processing the payment. Please try again later."

        return context


def charge(request):
    if request.method == 'POST':
        checkout_session_id = request.POST.get('checkout_session_id')

        if not checkout_session_id:
            return redirect('payment-error')

        try:
            session = stripe.checkout.Session.retrieve(checkout_session_id)
            if session.payment_status == 'paid':
                return redirect('payment-success')
            elif session.payment_status == 'unpaid':
                return redirect('payment-pending')
            elif session.payment_status == 'canceled':
                return redirect('payment-cancel')
            else:
                return redirect('')
        except error.StripeError as e:
            print("Stripe Error:", str(e))
            return render(request, 'payments/payment_error.html',
                          {'error_message': "An error occurred while processing the payment."})

    return render(request, 'payments/payment_success.html')


class ChargeSuccess(TemplateView):
    template_name = 'payments/payment_success.html'


class ChargeError(TemplateView):
    template_name = 'payments/payment_error.html'


class ChargePending(TemplateView):
    template_name = 'payments/payment_pending.html'


class ChargeCancel(TemplateView):
    template_name = 'payments/payment_cancel.html'
