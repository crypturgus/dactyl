import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = "Create a superuser"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.environ["DJANGO_SUPERUSER_USERNAME"]
        email = os.environ["DJANGO_SUPERUSER_EMAIL"]
        password = os.environ["DJANGO_SUPERUSER_PASSWORD"]

        try:
            User.objects.create_superuser(
                display_name=username, email=email, password=password
            )
            self.stdout.write(self.style.SUCCESS("Superuser created."))
        except IntegrityError:
            self.stdout.write(self.style.WARNING("Superuser already exists."))
