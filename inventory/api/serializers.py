from rest_framework import serializers

from inventory.models import Category


class CategorySerializer(serializers.ModelSerializer):

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
        return CategorySerializer(children, many=True).data


class CategrogyListCreateUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
