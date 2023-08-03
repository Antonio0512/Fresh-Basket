from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fresh_basket.accounts'

    def ready(self):
        import fresh_basket.accounts.signals
        result = super().ready()
        return result
