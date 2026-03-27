from django.shortcuts import render
from rest_framework import generics

from inventory.api.serializers import CategrogyListCreateUpdateDestroySerializer
from inventory.models import Category
from drf_spectacular.utils import extend_schema
from rest_framework.mixins import ListModelMixin


# Create your views here.
@extend_schema(tags=["inventory-Category"])
class CategrogyListCreateUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategrogyListCreateUpdateDestroySerializer
    lookup_field = "id"


@extend_schema(tags=["inventory-Category"])
class CategrogyListApiView(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategrogyListCreateUpdateDestroySerializer
