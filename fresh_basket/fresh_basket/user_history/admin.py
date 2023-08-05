from django.contrib import admin

from fresh_basket.user_history.models import UserView, UserCart, UserPurchase


@admin.register(UserView)
class RecordUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'timestamp')


@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'timestamp')


@admin.register(UserPurchase)
class UserPurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'timestamp')
