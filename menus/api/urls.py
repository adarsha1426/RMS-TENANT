from django.urls import include, path
from menus.api import views


urlpatterns = [
    # Food Category Routes
    path(
        "food-category/",
        include(
            [
                path("", views.FoodCategoryListCreateView.as_view()),
                path(
                    "<int:id>/", views.FoodCategoryRetireveUpdateDestroyView.as_view()
                ),
            ]
        ),
    ),
    # Menu Item Routes
    path(
        "menus-item/",
        include(
            [
                path("", views.MenuItemListCreateView.as_view()),
                path("<int:id>/", views.MenusItemRetireveUpdateDestroyView.as_view()),
            ]
        ),
    ),
]
