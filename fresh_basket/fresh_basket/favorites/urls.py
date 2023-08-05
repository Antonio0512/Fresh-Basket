from django.urls import path

from fresh_basket.favorites import views

urlpatterns = [
    path('products/', views.FavoriteListView.as_view(), name='favourites-products'),
    path('products/<int:pk>/add/', views.AddToFavoritesView.as_view(),
         name='add-to-favourites'),
    path('products/<int:pk>/remove/', views.RemoveFromFavouritesView.as_view(),
         name='remove-from-favourites'),
]
