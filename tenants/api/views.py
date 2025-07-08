from rest_framework.generics import ListCreateAPIView

from tenants.api.serializers import TenantSerialzer
from tenants.models import ResturantTenant

class  TenantListCreateView(ListCreateAPIView):
    queryset = ResturantTenant.objects.all()
    serializer_class = TenantSerialzer

    