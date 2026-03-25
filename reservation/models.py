from datetime import timezone

from django.db import models

from users.models import CustomUser
from utils.common_model import CommonModel
from utils.enums import TableStatusChoices


# Create your models here.
class Table(CommonModel):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    status = models.CharField(choices=TableStatusChoices.choices, default="completed")

    def __str__(self):
        return self.name


class Reservation(CommonModel):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="reserver"
    )
    phone = models.CharField(max_length=15)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    grace_time = models.CharField(max_length=100, help_text="in minutes")
    guests = models.IntegerField()

    def __str__(self):
        return f"{self.table.name} has been reserved for {self.start_time} - {self.end_time}"

    def get_guests(self):
        if self.guests > self.table.capacity:
            return f"Sorry!! The capacity of table is {self.table.capacity}. Please choose another table."

    def get_grace_time(self):
        return f"{self.grace_time} minutes"
