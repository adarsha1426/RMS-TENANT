from django.contrib import admin
from .models import Domain,ResturantTenant
# Register your models here.
class TenantAdminSite(admin.AdminSite):
    site_header = "Tenant Admin"

tenant_admin_site = TenantAdminSite(name="tenant_admin_site")

# Register models on your custom admin site instance
tenant_admin_site.register(Domain)
tenant_admin_site.register(ResturantTenant)