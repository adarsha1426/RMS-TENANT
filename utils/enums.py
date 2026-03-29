from django.db import models


class UserRole(models.TextChoices):
    """
    Resturant Owner
    Manager / admin --> Updated Inventory based on it -->staff
    Customer --> Reserves Table , Views Menu
    Superadmin --> Owner of SAAS product who can view all the resturant

    """

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


class TableStatusChoices(models.TextChoices):
    pending = "pending", "Pending"
    reserved = "reserved", "Reserved"
    completed = "completed", "Completed"
    cancelled = "cancelled", "Cancelled"
    new = "new", "New"


class UnitChoices(models.TextChoices):
    kg = "kg", "Kilogram"
    g = "g", "Gram"
    ltr = "ltr", "Liter"
    pcs = "pcs", "Pieces"


class ActionChoices(models.TextChoices):
    IN = "in", "IN"
    ADJUST = "adjust", "Adjust"
    OUT = "out", "OUT"
