from django.db import models

from users.models import CustomUser
from utils.common_model import CommonModel


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    items = models.CharField(max_length=100)
    units = models.CharField(max_length=10)  # like gram and kilogram
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    descripton = models.TextField()

    def __str__(self):
        return (
            f"{self.name} has been created under the category ->{self.category.name} "
        )


class InventoryLog(CommonModel):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    used_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    reason = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.inventory.name} used by {self.used_by} for {self.reason}"
