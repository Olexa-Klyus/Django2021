from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView, RetrieveDestroyAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from core.permissions.user_permissions import IsSuperUser

from apps.cars.serializers import CarSerializer

from .filters import AutoParkFilter
from .models import AutoParksModel
from .serializers import AutoParkSerializer

UserModel = get_user_model()


class AutoParksListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = (IsSuperUser,)
    filterset_class = AutoParkFilter

    # додаємо ту частину якої не вистачає
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owners=[user])


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


class AddOwnerToAutoParkView(GenericAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer

    def patch(self, *args, **kwargs):
        user = self.request.user
        auto_park = self.get_object()
        user_id = kwargs.get('user_id')
        new_owner = get_object_or_404(UserModel, pk=user_id)
        if auto_park.owners.filter(pk=user.id).exists():
            auto_park.owners.add(new_owner)
        return Response(self.serializer_class(auto_park).data)
