from django.urls import path

from . import views

urlpatterns = [
    path('all-products/', views.AllProductsListView.as_view(), name='products-all'),
    path('discount-products/', views.DiscountProductsListView.as_view(), name='products-discount'),
    path('all-products/product/<int:pk>/', views.ProductDetailsView.as_view(), name='product-details')
]
