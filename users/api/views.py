from users.api.serializers import (
    CustomTokenObtainPairSerializer,
    LoginSerializer,
    UserCreationSerializer,
    UserProfileCreateSerializer,
    UserProfileRetrieveUpdateSerializer,
)
from users.models import CustomUser, UserProfile

# django
from django.contrib.auth import authenticate
from django.shortcuts import render

# rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

# permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# utils
from utils.permissions import IsAdminUser

# jwt
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

# for drf documentation
from drf_spectacular.utils import OpenApiRequest, OpenApiResponse
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Login/Logout"], summary="Login View")
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@extend_schema(tags=["Login/Logout"])
class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password are required."}, status=400
            )

        user = authenticate(username=username, password=password)

        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "username": user.username,
                    "role": user.role,
                }
            )
        return Response({"error": "Invalid credentials"}, status=401)


@extend_schema(tags=["Login/Logout"], summary="Logout View")
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        rfrsh_token = request.data.get("refresh_token")
        try:
            token = RefreshToken(rfrsh_token)
            token.blacklist()
            return Response({"message": "Logout successful"})
        except (InvalidToken, TokenError):
            return Response(
                {"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST
            )


# @extend_schema(tags=["User "], summary="Sign Up for User")
class UserCreateView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [permissions.AllowAny]

    # def post(self, request, *args, **kwargs):
    #     user = request.data

    #     return self.create(request, *args, **kwargs)


@extend_schema(tags=["User Profile"], summary="User Creation")
class UserListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = UserCreationSerializer


@extend_schema(tags=["User Profile"], summary="User's Profile List URL")
class UserProfileListCreateView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileCreateSerializer


@extend_schema(
    tags=["User Profile"], summary="User Profile Rrtrieve Update and Delete URl"
)
class UserProfileRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileRetrieveUpdateSerializer
    lookup_field = "id"
