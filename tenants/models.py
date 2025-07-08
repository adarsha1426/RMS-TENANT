from django.db import models
from django_tenants.models import TenantMixin,DomainMixin
# Create your models here.


class ResturantTenant(TenantMixin):
    name = models.CharField(max_length=200)
    created  = models.DateField(auto_now_add=True)
    domain = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    on_trial = models.BooleanField()
    auto_create_schema = True

class Domain(DomainMixin):
    pass