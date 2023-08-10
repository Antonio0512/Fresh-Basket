from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth import get_user_model

UserModel = get_user_model()

@shared_task
def send_successful_registration_email(user_id):
    user = UserModel.objects.get(pk=user_id)

    html_message = render_to_string(
        'emails/email-greeting.html',
        {'user': user},
    )
    plain_message = strip_tags(html_message)

    send_mail(
        subject='Registration greetings',
        message=plain_message,
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
    )