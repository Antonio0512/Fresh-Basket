from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='page-home'),
    path('favourite-products/', views.FavoriteListView.as_view(), name='favourites-products'),
    path('favourites-products/<int:pk>/add/', views.AddToFavoritesView.as_view(),
         name='add-to-favourites'),
    path('favourites-products/<int:pk>/remove/', views.RemoveFromFavouritesView.as_view(),
         name='remove-from-favourites'),
    path('product/<int:pk>/reviews', views.ProductReviewsListView.as_view(), name='product-reviews'),
    path('product/<int:pk>/add/', views.AddReviewToProduct.as_view(), name='product-reviews-add')
]
