from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_successful_registration_email
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        send_successful_registration_email.delay(instance.id)
