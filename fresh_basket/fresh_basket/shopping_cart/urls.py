from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShoppingCartView.as_view(), name='shopping-cart'),
    path('add-to-cart/<int:product_id>/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('delete-from-cart/<int:product_id>/', views.DeleteFromCartView.as_view(), name='delete-from-cart')
]
