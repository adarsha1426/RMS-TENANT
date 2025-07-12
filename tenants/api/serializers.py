from rest_framework import serializers
from tenants.models import ResturantTenant


class TenantSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ResturantTenant
        fields = ["name", "created", "domain", "logo", "description", "on_trial"]

    def create(self, validated_data):
        name = validated_data.pop("name")
        domain = validated_data.pop("domain")
        logo = validated_data.pop("logo", None)
        description = validated_data.pop("description", None)
        on_trail = validated_data.pop("on_trial")
        resturant_tenant = ResturantTenant.objects.create(**validated_data)
        resturant_tenant.save()
        return resturant_tenant
