from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveDestroyAPIView

from .models import AutoParksModel
from .serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer


class AutoParksListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer


# клас для відображення одного автопарку і видалення автопарку по id
class AutoParksRetriveDestroyView(RetrieveDestroyAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer


# створити нове авто через автопарк
class AutoParkAddCarView(CreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = CarSerializer

    # щоб додати номер автопарку
    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)
