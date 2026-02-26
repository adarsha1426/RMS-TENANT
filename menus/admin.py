from django.contrib import admin

from menus.models import FoodCategory, MealType, MenuItem

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(FoodCategory)
admin.site.register(MealType)
