from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='page-home'),
    path('favourites-products/', views.FavoriteListView.as_view(), name='favourites-products'),
    path('favourites-products/add-to-favourites/<int:pk>', views.AddToFavoritesView.as_view(),
         name='add-to-favourites'),
    path('favourites-products/remove-from-favourites/<int:pk>', views.RemoveFromFavouritesView.as_view(),
         name='remove-from-favourites'),
    path('product/reviews/<int:pk>/', views.ProductReviewsListView.as_view(), name='product-reviews'),
    path('product/reviews/add-review/<int:pk>', views.AddReviewToProduct.as_view(), name='product-reviews-add')
]
