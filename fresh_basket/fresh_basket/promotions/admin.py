from django.contrib import admin
from . import models


@admin.register(models.Promotions)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
