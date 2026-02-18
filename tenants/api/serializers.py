from django.forms import ValidationError
from rest_framework import serializers
from tenants.models import Domain, ResturantTenant


class TenantSerializer(serializers.ModelSerializer):
    domain_name = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = ResturantTenant
        fields = [
            "id",
            "schema_name",
            "name",
            "logo",
            "description",
            "on_trial",
            "domain_name",
        ]

    def create(self, validated_data):
        domain_name = validated_data.pop("domain_name", None)
        if not ResturantTenant.objects.filter(
            schema_name=validated_data["schema_name"]
        ).exists():
            tenant = ResturantTenant.objects.create(**validated_data)

            Domain.objects.create(domain=domain_name, tenant=tenant, is_primary=True)
        else:
            raise ValidationError(f"Schema Name already exists")
        return tenant
