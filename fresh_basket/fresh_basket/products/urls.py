from django.urls import path

from . import views

urlpatterns = [
    path('products/all-products', views.AllProductsListView.as_view(), name='products-all'),
    path('products/discount-products', views.DiscountProductsListView.as_view(), name='products-discount'),
]
