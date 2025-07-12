from django.db import models


class UserRole(models.TextChoices):
    ADMIN = "admin", "Admin"
    STAFF = "staff", "Staff"
    CUSTOMER = "customer", "Customer"


class AuthProvider(models.TextChoices):
    google = "google", "google"
    facebook = "facebook", "Facebook"
    github = "github", "Github"
    email = "email", "Email"


class GenderChoice(models.TextChoices):
    male = "male", "Male"
    female = "female", "Female"
    others = "others", "others"
