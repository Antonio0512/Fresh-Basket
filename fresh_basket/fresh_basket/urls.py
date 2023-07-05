from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fresh_basket.common.urls')),
    path('accounts/', include('fresh_basket.accounts.urls'))
]
