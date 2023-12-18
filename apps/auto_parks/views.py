from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from core.permissions.user_permissions import IsSuperUser

from apps.cars.serializers import CarSerializer

from .models import AutoParksModel
from .serializers import AutoParkSerializer


class AutoParksListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = (IsSuperUser,)


# клас для відображення одного автопарку і видалення автопарку по id
class AutoParksRetriveDestroyView(RetrieveDestroyAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = (AllowAny,)

    # якщо для кожного метода робити свій пермішин, витягаємо з селфу метод і викликаємо для нього дозвіл
    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [AllowAny()]

        return super().get_permissions()


# створити нове авто через автопарк з використанням perform_create
class AutoParkAddCarView(CreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # щоб додати номер автопарку є метод
    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)
