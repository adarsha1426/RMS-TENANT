from django.db import models

from users.models import CustomUser
from utils.common_model import CommonModel
from utils.enums import ActionChoices, UnitChoices


# Create your models here.


class Category(CommonModel):
    """
    example:
        name = vegetables type ingredients
        name = knife Type = Cutlery parent = ASSEST
    """

    name = models.CharField(max_length=100)

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subcategories",
    )

    class Meta:
        unique_together = [
            ("name", "parent"),
        ]

    def __str__(self):
        return f"{self.name}"


class Inventory(CommonModel):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    units = models.CharField(max_length=10, choices=UnitChoices)  # like g and kg
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return (
            f"{self.name} has been created under the category ->{self.category.name} "
        )


class InventoryLog(CommonModel):
    inventory = models.ForeignKey(Inventory, on_delete=models.PROTECT)
    action = models.CharField(max_length=10, choices=ActionChoices)
    used_by = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True
    )
    reason = models.TextField()
    previous_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    new_quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        username = self.used_by.username if self.used_by else "Unknown User"
        return f"{username} has  {self.action} for {self.reason}"
