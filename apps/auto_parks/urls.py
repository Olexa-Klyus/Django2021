from django.urls import path

from .views import AutoParkAddCarView, AutoParksListCreateView, AutoParksRetriveDestroyView

urlpatterns = [
    path('', AutoParksListCreateView.as_view()),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view()),
    path('/<int:pk>', AutoParksRetriveDestroyView.as_view())
]
