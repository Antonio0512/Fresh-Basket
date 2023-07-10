from django.shortcuts import render

from fresh_basket.promotions.models import Promotions


def home(request):
    promotions = Promotions.objects.all()

    context = {
        'promotions': promotions
    }
    return render(request, 'common/home.html', context)