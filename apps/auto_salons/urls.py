from django.urls import path

from .views import AutoSalonListCreateView

urlpatterns = [
    path('', AutoSalonListCreateView.as_view())
]