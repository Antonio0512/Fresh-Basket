from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllPromotionsListView.as_view(), name='promotions-all')
]
