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


from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "token/",
        include(
            [
                path("", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
                path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
            ]
        ),
    ),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path(
        "profile/",
        include(
            [
                path("create/", UserProfileListCreateView.as_view()),
                path("<int:id>/", UserProfileRetrieveUpdateView.as_view()),
            ]
        ),
    ),
    path("", UserListView.as_view()),
    path("create/", UserCreateView.as_view()),
]
