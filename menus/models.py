from django.db import models

from utils.common_model import CommonModel


# Create your models here.
class FoodCategory(CommonModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="category/", null=True, blank=True)

    def __str__(self):
        return self.name


class MealType(models.Model):
    meal_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.meal_type


class MenuItem(CommonModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    price = models.DecimalField(max_digits=8, decimal_places=2)
    discounted_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )

    category = models.ForeignKey(
        FoodCategory, on_delete=models.CASCADE, related_name="items"
    )

    image = models.ImageField(upload_to="menu/", null=True, blank=True)

    is_available = models.BooleanField(default=True)
    is_veg = models.BooleanField(default=False)
    is_featured = models.BooleanField(
        default=False
    )  # to highlight them in dashboard or menu for future

    preparation_time = models.IntegerField(
        help_text="in minutes", null=True, blank=True
    )
    code = models.CharField(help_text="SKU code", max_length=10, unique=True)
    meal_type = models.ManyToManyField(MealType, blank=True)

    def __str__(self):
        return self.name
