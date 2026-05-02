from django.core.cache import cache
from rest_framework import request
from django_redis import get_redis_connection


class TenantRedisService:
    def __init__(self, prefix):
        self.prefix = prefix

    def key(self, key):
        return f"{self.prefix}:{key}"

    def get(self, key):
        return cache.get(self.key(key))

    def set(self, key, value, timeout=300):
        cache.set(self.key(key), value, timeout)

    def delete(self, key):
        cache.delete(self.key(key))

    def delete_pattern(self, pattern):
        conn = get_redis_connection("default")
        keys = conn.keys(f"{self.prefix}:{pattern}")
        if keys:
            conn.delete(*keys)
