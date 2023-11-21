from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from rest_framework.response import Response

from .models import CarModel
from .serializers import CarSerializer
from rest_framework import status


# якщо робити через APIView

# CRUD
# create
# read/retrive
# update
# delete/destroy

# class CarListCreateView(APIView):
#     def get(self, *args, **kwargs):
#         cars = CarModel.objects.all()
#         # print(cars.query)
#
#         # використання фільтрів
#         # cars = cars.filter(brand='bmw', price=6000)
#         # cars = cars.filter(brand__in=('bmw', 'audi'))
#         # cars = cars.filter(brand__icontains='b')
#         # cars = cars.filter(price__range=(3000, 8000))
#
#         # можна імпортнути і використовувати Q
#         # cars = cars.filter(Q(price=4000) | Q(price=6000) | Q(brand='bmw'))
#         # cars = cars.filter(Q(price=4000) | Q(price=6000), brand='bmw')
#
#         # може бути фільтр від фільтра або сорт. Якщо спадання - знак мінус
#         # cars = cars.filter(price__gt=3000).order_by('-price', 'year')[:2]
#
#         # поки запит не виконався, а тільки сформувався, можна роздрукувати і cars.query cars.count
#         # коли запит виконався в базі, цих властивостей вже нема
#         # print(cars.count())
#         # print(cars.query)
#
#         price_gt = self.request.query_params.get('price_gt')
#         if price_gt:
#             cars = cars.filter(price__gt=price_gt)
#         print(cars.query)
#
#         serializer = CarSerializer(instance=cars, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         # car = CarModel.objects.create(**data) запис в базу тепер зробить серіалайзер під капотом своїм save()
#
#         serializer = CarSerializer(data=data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         print(serializer.data)
#         return Response(serializer.data, status.HTTP_201_CREATED)

# class CarUpdateRetriveDestroy(APIView):
#     def get(self, *args, **kwargs):
#         car_id = kwargs.get('pk')
#
#         if not CarModel.objects.filter(pk=car_id).exists():
#             return Response('Car with this id not found', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=car_id)
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         data = self.request.data
#
#         car_id = kwargs.get('pk')
#         if not CarModel.objects.filter(pk=car_id).exists():
#             return Response('Car with this id not found', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=car_id)
#         serializer = CarSerializer(car, data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors)
#         # цю перевірку записуємо коротше
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         data = self.request.data
#
#         car_id = kwargs.get('pk')
#         if not CarModel.objects.filter(pk=car_id).exists():
#             return Response('Car with this id not found', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=car_id)
#         serializer = CarSerializer(car, data, partial=True)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors)
#         # цю перевірку записуємо коротше
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if not CarModel.objects.filter(pk=pk).exists():
#             return Response('Car with this id not found', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=pk)
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# якщо робити через GenericAPIView


# class CarListCreateView(GenericAPIView):
#
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         cars = self.get_queryset()
#
#         serializer = self.serializer_class(instance=cars, many=True)
#
#         return Response(serializer.data, status.HTTP_200_OK)
#
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         # car = CarModel.objects.create(**data) запис в базу тепер зробить серіалайзер під капотом своїм save()
#
#         serializer = CarSerializer(data=data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         print(serializer.data)
#         return Response(serializer.data, status.HTTP_201_CREATED)


# class CarUpdateRetriveDestroy(GenericAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#
#         car = self.get_object()
#         serializer = self.serializer_class(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         data = self.request.data
#
#         car_id = kwargs.get('pk')
#         if not CarModel.objects.filter(pk=car_id).exists():
#             return Response('Car with this id not found', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=car_id)
#         serializer = CarSerializer(car, data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors)
#         # цю перевірку записуємо коротше
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         data = self.request.data
#
#         car_id = kwargs.get('pk')
#         if not CarModel.objects.filter(pk=car_id).exists():
#             return Response('Car with this id not found', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=car_id)
#         serializer = CarSerializer(car, data, partial=True)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors)
#         # цю перевірку записуємо коротше
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if not CarModel.objects.filter(pk=pk).exists():
#             return Response('Car with this id not found', status.HTTP_404_NOT_FOUND)
#
#         car = CarModel.objects.get(pk=pk)
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class CarListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):  # за допомогою міксінів
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get(self, *args, **kwargs):
        return super().list(self.request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return super().create(self.request, *args, **kwargs)


class CarUpdateRetriveDestroy(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get(self, *args, **kwargs):
        return super().retrieve(self.request, *args, **kwargs)

