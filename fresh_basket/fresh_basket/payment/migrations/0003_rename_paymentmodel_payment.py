# Generated by Django 4.2.3 on 2023-07-26 08:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0002_rename_payment_paymentmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PaymentModel',
            new_name='Payment',
        ),
    ]
