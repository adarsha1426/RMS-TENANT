from rest_framework.generics import ListCreateAPIView

from tenants.api.serializers import TenantSerialzer
from tenants.models import ResturantTenant
from rest_framework import permissions

from utils.permissions import IsAdminUser
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Create New Resturant "], summary="For SuperAdmin only")
class TenantListCreateView(ListCreateAPIView):
    queryset = ResturantTenant.objects.all()
    serializer_class = TenantSerialzer
    permission_classes = [IsAdminUser]
