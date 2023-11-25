from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveDestroyAPIView, GenericAPIView
from rest_framework.response import Response

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


# створити нове авто через автопарк з використанням perform_create
# class AutoParkAddCarView(CreateAPIView):
#     queryset = AutoParksModel.objects.all()
#     serializer_class = CarSerializer
#
#     # щоб додати номер автопарку є метод
#     def perform_create(self, serializer):
#         auto_park = self.get_object()
#         serializer.save(auto_park=auto_park)

# або через звичайний дженерік
class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParksModel
    serializer_class = CarSerializer

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        car = self.request.data
        serializer = self.serializer_class(data=car)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        return Response(serializer.data, status.HTTP_200_OK)
