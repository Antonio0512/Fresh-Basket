from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fresh_basket.common.urls')),
    path('reviews/', include('fresh_basket.reviews.urls')),
    path('favorites/', include('fresh_basket.favorites.urls')),
    path('accounts/', include('fresh_basket.accounts.urls')),
    path('products/', include('fresh_basket.products.urls')),
    path('promotions/', include('fresh_basket.promotions.urls')),
    path('catalog/', include('fresh_basket.catalog.urls')),
    path('shopping-cart/', include('fresh_basket.shopping_cart.urls')),
    path('payment/', include('fresh_basket.payment.urls')),
    path('user_history/', include('fresh_basket.user_history.urls')),
    path('blog/', include('fresh_basket.blog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
