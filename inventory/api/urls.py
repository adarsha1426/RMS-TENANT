from django.urls import path, include

from inventory.api.views import (
    CategrogyListApiView,
    CategrogyListCreateUpdateDestroyView,
)

urlpatterns = [
    path("category/<int:id>/", CategrogyListCreateUpdateDestroyView.as_view()),
    path("category/", CategrogyListApiView.as_view()),
]
