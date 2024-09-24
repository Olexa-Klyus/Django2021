from django.urls import path

from .views import CarListCreateView, CarUpdateRetrieveDestroy

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarUpdateRetrieveDestroy.as_view())
]
