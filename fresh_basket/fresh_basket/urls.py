from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fresh_basket.common.urls')),
    path('accounts/', include('fresh_basket.accounts.urls')),
    path('products/', include('fresh_basket.products.urls')),
    path('catalog/', include('fresh_basket.catalog.urls')),
    path('shopping-cart/', include('fresh_basket.shopping_cart.urls')),
    path('payment/', include('fresh_basket.payment.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
