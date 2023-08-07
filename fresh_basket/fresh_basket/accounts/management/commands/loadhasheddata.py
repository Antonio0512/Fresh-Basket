from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

MyUser = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = [
            {
                "pk": 3,
                "username": "Gosho",
                "email": "antonioboyanov9test+test3@gmail.com",
                "password": make_password("toni1234")
            },
            {
                "pk": 4,
                "username": "Ivan",
                "email": "antonioboyanov9test+test4@gmail.com",
                "password": make_password("toni1234"),
            },
        ]

        MyUser.objects.bulk_create([MyUser(**item) for item in data])

# activation - python manage.py loadhasheddata