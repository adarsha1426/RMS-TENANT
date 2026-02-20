from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

from users.api.views import (
    CustomTokenObtainPairView,
    LoginView,
    LogoutView,
    UserCreateView,
    UserListView,
    UserProfileListCreateView,
    UserProfileRetrieveUpdateView,
)


urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("", UserListView.as_view()),
    path("profile/create", UserProfileListCreateView.as_view()),
    path("create/", UserCreateView.as_view()),
    path("profile/<int:id>/", UserProfileRetrieveUpdateView.as_view()),
]
