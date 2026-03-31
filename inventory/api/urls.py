from django.urls import path, include

from inventory.api.views import (
    CategrogyListCreateApiView,
    CategrogyListCreateUpdateDestroyView,
    InventoryListCreateView,
    InventoryLogListView,
    InventoryRetrieveUpdateDestroy,
)

urlpatterns = [
    path(
        "category/",
        include(
            [
                path(
                    "<int:id>/",
                    CategrogyListCreateUpdateDestroyView.as_view(),
                ),
                path("", CategrogyListCreateApiView.as_view()),
            ]
        ),
    ),
    path(
        "inventory-item/",
        include(
            [
                path("", InventoryListCreateView.as_view()),
                path("<int:id>/update/", InventoryRetrieveUpdateDestroy.as_view()),
            ]
        ),
    ),
    path("inventory-log", InventoryLogListView.as_view()),
]
