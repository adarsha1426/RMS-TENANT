from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from utils.services import TenantRedisService

from .models import MenuItem
from django.db import connection


@receiver([pre_save, post_delete], sender=MenuItem)
def invalidate_menu_item_list(sender, instance, **kwargs):
    tenant = connection.tenant

    if tenant:
        print(f"{tenant.schema_name} signal name has been called.")
        redis_service = TenantRedisService(tenant.schema_name)
        redis_service.delete("menu-item-list")
        redis_service.delete_pattern("*menu-item-list*")
