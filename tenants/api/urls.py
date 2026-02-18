from tenants.api.views import TenantListCreateView
from django.urls import path

urlpatterns = [path("create/", TenantListCreateView.as_view())]
