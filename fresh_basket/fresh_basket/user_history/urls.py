from django.urls import path
from . import views

urlpatterns = [
    path('record-user-view/<int:product_id>/', views.record_user_view, name='record-user-view'),
    path('record-user-cart/<int:product_id>/', views.record_user_cart, name='record-user-cart'),
    path('record-user-purchase/<int:product_id>/', views.record_user_purchase, name='record-user-purchase')

]
