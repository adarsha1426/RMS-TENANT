from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from users.api.serializers import (
    UserCreationSerializer,
    UserProfileCreateSerializer,
    UserProfileRetrieveUpdateSerializer,
)
from users.models import CustomUser, UserProfile


# Create your views here.
class UserCreateView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreationSerializer


class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreationSerializer


class UserProfileListCreateView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileCreateSerializer


class UserProfileRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileRetrieveUpdateSerializer
    lookup_field = "id"
