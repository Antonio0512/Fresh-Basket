from django.urls import path

from . import views

urlpatterns = [
    path('all-products/', views.AllProductsListView.as_view(), name='products-all'),
    path('discount-products/', views.DiscountProductsListView.as_view(), name='products-discount'),
    path('all-products/<int:pk>/', views.ProductDetailsView.as_view(), name='all-product-details'),
    path('discount-products/<int:pk>/', views.ProductDetailsView.as_view(), name='discount-product-details'),
    path('favourite-products/<int:pk>/', views.ProductDetailsView.as_view(),
         name='favourite-products-details'),
    path('recommended-products/<int:pk>/', views.ProductDetailsView.as_view(), name='recommended-product-details'),
    path('cart/product/<int:pk>/', views.ProductDetailsView.as_view(), name='cart-details'),
]
