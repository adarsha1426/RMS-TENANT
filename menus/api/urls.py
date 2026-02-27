from django.urls import path
from menus.api import views

urlpatterns = [
    path("menus-item", views.MenuItemListCreateView.as_view()),
    path("food-category", views.FoodCategoryListCreateView.as_view()),
    path(
        "food-category/<int:id>/", views.FoodCategoryRetireveUpdateDestroyView.as_view()
    ),
    path("menus-item/<int:id>", views.MenusItemRetireveUpdateDestroyView.as_view()),
]
