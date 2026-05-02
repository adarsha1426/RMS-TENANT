from django.urls import path, include
from .views import (
    TableListCreateView,
    TableListView,
    TableReserveListCreateView,
    TableReserverRetireveUpdateDestroyView,
    TableRetrieveUpdateDestroyView,
)

app_name = "reservation"
urlpatterns = [
    path("", TableListView.as_view()),
    path("create/", TableListCreateView.as_view()),
    path("<int:id>/", TableRetrieveUpdateDestroyView.as_view()),
    path("reservation/", TableReserveListCreateView.as_view()),
    path(
        "<int:table_id>/reservation/",
        include(
            [
                path("<int:id>/", TableReserverRetireveUpdateDestroyView.as_view()),
            ]
        ),
    ),
]
