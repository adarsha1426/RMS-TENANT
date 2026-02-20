from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms import ValidationError

from utils.enums import AuthProvider, GenderChoice, UserRole
from utils.common_model import CommonModel


class CustomUserModel(BaseUserManager):
    def create_user(
        self,
        username,
        password,
        email,
        role,
        first_name=None,
        middle_name=None,
        last_name=None,
        **kwargs,
    ):
        if not username:
            raise ValidationError({"error": "Username is required."})
        if not password:
            raise ValueError({"error": "Password is required"})
        if not email:
            raise ValueError({"error": "Email is required"})
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            role=role,
            email=email,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_admin", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)
        return self.create_user(
            username, password, email, role=UserRole.ADMIN, **kwargs
        )


# Create your models here.
class CustomUser(AbstractBaseUser, CommonModel):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserModel()
    role = models.CharField(
        max_length=20, choices=UserRole.choices, default=UserRole.CUSTOMER
    )

    auth_provider = models.CharField(
        max_length=20,
        choices=AuthProvider.choices,
        default="email",
    )

    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    class Meta:
        db_table = "custom_user"

    def __str__(self):
        return f"{self.username} has role {self.role}"

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    @property
    def get_full_name(self):
        if not self.middle_name:
            return f"{self.first_name} {self.last_name}"
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class UserProfile(CommonModel):
    user = models.OneToOneField(
        CustomUser, unique=True, related_name="profile", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="media/profile_images/", blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoice,
        blank=True,
        null=True,
    )

    @property
    def get_full_name(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        elif self.user.first_name and self.user.middle_name:
            return (
                f"{self.user.first_name} {self.user.middle_name} {self.user.last_name}"
            )
        else:
            return ""
