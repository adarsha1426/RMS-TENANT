from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from menus.api.serializers import (
    FoodCategoryListCreateSerializer,
    MealTypeListCreateSeializer,
    MenuItemListCreateSerializer,
    MenuItemRetrieveUpdateDestroySeiralizer,
)
from menus.models import FoodCategory, MealType, MenuItem
from utils.permissions import IsAdminUser


# Create your views here.\
@extend_schema(tags=["Food-Item"], summary="Food-Item-Category")
class FoodCategoryListCreateView(generics.ListCreateAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategoryListCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.IsAuthenticated()]
        return [IsAdminUser()]


@extend_schema(tags=["Food-Category"])
class FoodCategoryRetireveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategoryListCreateSerializer


@extend_schema(tags=["Food-Item"], summary="Meal-Type-Category")
class MealTypeListCreateView(generics.ListCreateAPIView):
    queryset = MealType.objects.all()
    serializer_class = MealTypeListCreateSeializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.IsAuthenticated()]
        return [IsAdminUser()]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@extend_schema(tags=["Menu-Item"], summary="Menu-Item")
class MenuItemListCreateView(generics.ListCreateAPIView):

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemListCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.IsAuthenticated()]
        return [IsAdminUser()]

    @method_decorator(cache_page(60 * 15, key_prefix="menu-item-list"))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


@extend_schema(tags=["Menu-Item"], summary="Menu-Item")
class MenusItemRetireveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemRetrieveUpdateDestroySeiralizer
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
