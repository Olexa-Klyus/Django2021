from django.urls import path

from .views import CarListCreateView, CarUpdateRetriveDestroy

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarUpdateRetriveDestroy.as_view())
]
