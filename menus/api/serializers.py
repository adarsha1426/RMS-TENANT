from menus.models import MenuItem, MealType, FoodCategory
from rest_framework.serializers import ModelSerializer


class FoodCategoryListCreateSerializer(ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = "__all__"


class MealTypeListCreateSeializer(ModelSerializer):
    class Meta:
        model = MealType
        fields = "__all__"


class MenuItemListCreateSerializer(ModelSerializer):

    class Meta:
        model = MenuItem
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["name"] = instance.name.capitalize()
        rep["meal_type"] = {"id": instance.id, "name": instance.name}
        rep["category"] = {"id": instance.category.id, "name": instance.category.name}
        rep["category_name"] = instance.category.name if instance.category else None
        return rep


class MenuItemRetrieveUpdateDestroySeiralizer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["name"] = instance.name.capitalize()
        # rep["meal_type"] = {"id": instance.id, "meal_type": instance.meal_type}
        rep["category"] = {"id": instance.category.id, "name": instance.category.name}
        rep["category_name"] = instance.category.name if instance.category else None
        return rep

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        meal_type = data.pop("meal_type").items()
        """
       "meal_type": {
            "id": 1,
            "name": "Thakali Khana"
            }
        """
        meal = MealType.objects.filter(id=meal_type["id"])
        if meal.exists():
            MealType.objects.update(meal_type=meal_type["meal_type"])
        return data
