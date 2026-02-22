from django.core.management.base import (
    BaseCommand,
)  # This is use to create custom django command run via manage.py
from django_tenants.utils import schema_context
from django.contrib.auth.hashers import make_password

from users.models import CustomUser


class Command(BaseCommand):
    help = "Create a user specific tenant schmes"

    def add_arguments(self, parser):
        parser.add_argument(
            "--schema",
            type=str,
            required=True,
            help="Tenant Scheme name (eg littlelemonresturant)",
        )
        parser.add_argument(
            "--username", type=str, required=True, help="Username for user"
        )
        parser.add_argument(
            "--email", type=str, required=True, help="Email is required"
        )
        parser.add_argument(
            "--password", type=str, required=True, help="password is required."
        )

    def handle(self, *args, **kwargs):
        schema = kwargs["schema"]
        username = kwargs["username"]
        email = kwargs["email"]
        password = kwargs["password"]

        with schema_context(schema):
            if CustomUser.objects.filter(username=username).exists():
                return self.stdout.write(
                    self.style.WARNING(
                        f"User with {username} already exists in schema {schema}"
                    )
                )
            elif CustomUser.objects.filter(email=email).exists():
                return self.stdout.wirte(
                    self.style.WARNING(
                        f"User with {email} already exists in schema {schema}"
                    )
                )
            else:
                CustomUser.objects.create(
                    username=username,
                    email=email,
                    password=make_password(password),
                    is_staff=True,
                    is_superuser=True,
                    is_admin=True,
                    role="admin",
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"{username} created successfully with email {email} in schema {schema}"
                    )
                )
