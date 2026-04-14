from django.contrib import admin
from django.urls import path, include
from tenants.admin import tenant_admin_site

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("admin_public/", tenant_admin_site.urls),
    path(
        "api/",
        include(
            [
                path(
                    "api-auth/",
                    include("rest_framework.urls", namespace="rest_framework"),
                ),
                path("user/", include("users.api.urls")),
                path("accounts/", include("allauth.urls")),
                path("menus/", include("menus.api.urls")),
                path("tables/", include("reservation.api.urls")),
                path("inventory/", include("inventory.api.urls")),
                path("schema/", SpectacularAPIView.as_view(), name="schema"),
                path(
                    "swagger/",
                    SpectacularSwaggerView.as_view(url_name="schema"),
                    name="swagger-ui",
                ),
                path(
                    "schema/redoc/",
                    SpectacularRedocView.as_view(url_name="schema"),
                    name="redoc",
                ),
            ],
        ),
    ),
    path("accounts/", include("allauth.urls")),
]
