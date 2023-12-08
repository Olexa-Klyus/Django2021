from django.urls import path

from .views import CarListView, CarUpdateRetriveDestroy

urlpatterns = [
    path('', CarListView.as_view()),
    path('/<int:pk>', CarUpdateRetriveDestroy.as_view())
]
