from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from reservation.api.serializers import (
    ReservationRetirieveUpdateDestroySerializer,
    ReservationSerializer,
    TableCreateSerializer,
    TableListSerializer,
    TableRetireveUpdateDestroySerializer,
)
from rest_framework import generics

from reservation.models import Reservation, Table
from utils.permissions import IsAdminUser

from rest_framework import permissions
from rest_framework.response import Response


# Create your views here.
@extend_schema(tags=["Tables"])
class TableListView(generics.ListAPIView):
    queryset = Table.objects.all()
    # serializer_class = TableListSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "GET":
            return TableListSerializer
        elif self.request.method == "POST":
            return TableCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        else:
            return [IsAdminUser()]


@extend_schema(tags=["Tables"])
class TableListCreateView(generics.CreateAPIView):
    queryset = Table.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "GET":
            return TableListSerializer
        elif self.request.method == "POST":
            return TableCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        else:
            return [IsAdminUser()]


@extend_schema(tags=["Tables"])
class TableRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableRetireveUpdateDestroySerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id"


@extend_schema(tags=["Table Reserved "])
class TableReserveListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Table Reserved "])
class TableReserverRetireveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationRetirieveUpdateDestroySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = ReservationRetirieveUpdateDestroySerializer(obj)
        return Response({"message": "Retrieved", "data": serializer.data}, status=200)
