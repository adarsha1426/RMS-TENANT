import requests
from inventory.models import Inventory, InventoryLog


def create_inventory_log(data, request):
    inventory = Inventory.objects.create(**data)
    user = request.user

    InventoryLog.objects.create(
        inventory=inventory,
        used_by=user,
        previous_quantity=0.0,
        new_quantity=inventory.quantity,
        action="In",
        reason="Initial Creation of inventory items",
    )
    return inventory


def update_stock_log(request, inventory_id, quantity, reason, action):

    inventory = Inventory.objects.get(id=inventory_id)

    previous_quantity = inventory.quantity
    if action == "in":
        inventory.quantity += quantity
        new_quantity = inventory.quantity

    elif action == "out":
        if quantity > inventory.quantity:
            raise ValueError("Not enough stock")
        inventory.quantity -= quantity
    elif action == "adjust":
        new_quantity = quantity  # quantity is the final value
        inventory.quantity = new_quantity
    else:
        raise ValueError("Invalid action choice")

    InventoryLog.objects.create(
        inventory_id=inventory_id,
        reason=reason,
        action=action,
        previous_quantity=previous_quantity,
        new_quantity=new_quantity,
        used_by=request.user,
    )

    return inventory
