from rest_framework.generics import ListCreateAPIView

from tenants.api.serializers import (
    TenantSerializer,
)
from tenants.models import ResturantTenant


from utils.permissions import IsAdminUser
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Create New Resturant "], summary="For SuperAdmin only")
class TenantListCreateView(ListCreateAPIView):
    serializer_class = TenantSerializer
    queryset = ResturantTenant.objects.all()
    permission_classes = [IsAdminUser]
