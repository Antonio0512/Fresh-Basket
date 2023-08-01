from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaymentView.as_view(), name='payment-home'),
    path('charge/', views.charge, name='charge'),
    path('charge-success/', views.ChargeSuccess.as_view(), name='payment-success'),
    path('charge-cancel/', views.ChargeCancel.as_view(), name='payment-cancel'),
    path('charge-error/', views.ChargeError.as_view(), name='payment-error'),
    path('charge-pending/', views.ChargePending.as_view(), name='payment-pending'),
]
