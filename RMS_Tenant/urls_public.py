from django.contrib import admin
from django.urls import path, include
from tenants.admin import tenant_admin_site
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", tenant_admin_site.urls),
    # path(
    #     "api/",
    #     include(
    #         [
    #             path("tenant/", include("tenants.api.urls")),
    #             path("user/", include("users.api.urls")),
    #             path("menus/", include("menus.api.urls")),
    #             path(
    #                 "swagger/",
    #                 SpectacularSwaggerView.as_view(url_name="schema"),
    #             ),
    #             path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    #         ]
    #     ),
    # ),
]
