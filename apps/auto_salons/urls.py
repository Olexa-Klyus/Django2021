from django.urls import path

from .views import AutoSalonsListCreateView, AutoSalonsListView

urlpatterns = [
    path('/user', AutoSalonsListCreateView.as_view()),
    path('/all', AutoSalonsListView.as_view())
]