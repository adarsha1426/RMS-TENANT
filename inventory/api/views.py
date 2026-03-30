from django.shortcuts import render
from rest_framework import generics, permissions

from inventory.api.serializers import (
    CategoryListCreateSerializer,
    CategrogyListCreateUpdateDestroySerializer,
    InventoryListCreateSerialzier,
    InventoryLogSerializer,
    InventoryRetrieveUpdateDestroySerializer,
)
from inventory.models import Category, Inventory, InventoryLog
from drf_spectacular.utils import extend_schema
from rest_framework.mixins import ListModelMixin, Response

from inventory.services import create_inventory_log, update_stock_log


# Create your views here.
@extend_schema(tags=["inventory-Category"])
class CategrogyListCreateUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategrogyListCreateUpdateDestroySerializer
    lookup_field = "id"


@extend_schema(tags=["inventory-Category"])
class CategrogyListCreateApiView(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategoryListCreateSerializer


@extend_schema(tags=["inventory-item"])
class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryListCreateSerialzier

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            create_inventory_log(data=serializer.validated_data, request=self.request)
            return Response(serializer.data)


@extend_schema(tags=["inventory-items"])
class InventoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryRetrieveUpdateDestroySerializer
    lookup_field = "id"

    def perform_update(self, serializer):

        instance = serializer.save()

        quantity = self.request.data.get("quantity")
        action = self.request.data.get("action")
        reason = self.request.data.get("reason")

        if quantity and action:

            update_stock_log(
                request=self.request,
                inventory_id=instance.id,
                quantity=int(quantity),
                action=action,
                reason=reason or "Manual update",
            )


@extend_schema(tags=["invetory-log"])
class InventoryLogListView(generics.ListAPIView):
    queryset = InventoryLog.objects.all()
    serializer_class = InventoryLogSerializer
    permission_classes = [permissions.AllowAny]
