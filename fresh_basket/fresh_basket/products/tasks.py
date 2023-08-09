import os
# import datetime

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

UserModel = get_user_model()


@shared_task
def send_sunday_email():
    # now = datetime.datetime.now()
    #
    # if now.weekday() == 2 and now.hour == 16 and now.minute == 57:
    users = UserModel.objects.all()

    for user in users:
        html_message = render_to_string(
            'emails/email-discounts-remainder.html',
            {user: user}
        )
        plain_message = strip_tags(html_message)

        send_mail(
            subject='Sunday Discount Reminder',
            message=plain_message,
            html_message=html_message,
            from_email=os.environ.get('EMAIL_HOST_USER'),
            recipient_list=[user.email],
        )

