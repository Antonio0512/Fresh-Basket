import stripe
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentView(TemplateView):
    template_name = "payments/payment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request):
    if request.method == 'POST':
        stripe.Charge.create(
            amount=500,
            currency='USD',
            description='A Django payment',
            source=request.POST['stripeToken']
        )

        return render(request, 'payments/charge.html')