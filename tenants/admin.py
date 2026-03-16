from django.contrib import admin
from .models import Domain, ResturantTenant

from users.models import CustomUser

from django.contrib.admin import ModelAdmin


# Register your models here.
class TenantAdminSite(admin.AdminSite):
    site_header = "Tenant Admin"
    list_display = (
        "name",
        "domain",
        "paid_until",
    )


tenant_admin_site = TenantAdminSite(name="tenant_admin_site")

# Register models on your custom admin site instance
tenant_admin_site.register(Domain)
tenant_admin_site.register(ResturantTenant)
tenant_admin_site.register(CustomUser)
