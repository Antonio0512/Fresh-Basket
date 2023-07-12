from django.urls import path

from . import views

urlpatterns = [
    path('all-products/', views.AllProductsListView.as_view(), name='products-all'),
    path('discount-products/', views.DiscountProductsListView.as_view(), name='products-discount'),
    path('all-products/product/<int:pk>/', views.ProductDetailsView.as_view(), name='all-product-details'),
    path('discount-products/product/<int:pk>/', views.ProductDetailsView.as_view(), name='discount-product-details'),
    path('favourite-products/product/<int:pk>/', views.ProductDetailsView.as_view(),
         name='favourite-products-details'),
    path('cart/product/<int:pk>/', views.ProductDetailsView.as_view(), name='cart-details'),
]
