from rest_framework import serializers

from inventory.models import Category, Inventory, InventoryLog
from utils.enums import ActionChoices


class CategoryListCreateSerializer(serializers.ModelSerializer):

    subcategories = serializers.SerializerMethodField()
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Category
        fields = ["id", "name", "parent", "subcategories"]

    def get_subcategories(self, obj):
        children = obj.subcategories.all()  # children --> subcategory
        return CategoryListCreateSerializer(children, many=True).data


class CategrogyListCreateUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class InventoryListCreateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class InventoryRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    reason = serializers.CharField(max_length=100, write_only=True)
    action = serializers.ChoiceField(choices=ActionChoices, write_only=True)

    class Meta:
        model = Inventory
        fields = "__all__"


class InventoryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryLog
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["username"] = instance.used_by.username
        data["category"] = instance.inventory.category.name
        data.pop("inventory")
        data.pop("used_by")
        return data
