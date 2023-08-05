from django.urls import path

from fresh_basket.reviews import views

urlpatterns = [
    path('product/<int:pk>/reviews', views.ProductReviewsListView.as_view(), name='product-reviews'),
    path('product/<int:pk>/add/', views.AddReviewToProduct.as_view(), name='product-reviews-add')
]
