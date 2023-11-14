from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CarModel
from .serializers import CarSerializer


# CRUD
# create
# read/retrive
# update
# delete/destroy

class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarSerializer(instance=cars, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        # car = CarModel.objects.create(**data) запис в базу тепер зробить серіалайзер під капотом своїм save()

        serializer = CarSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)


class CarUpdateRetriveDestroy(APIView):
    def get(self, *args, **kwargs):
        car_id = kwargs.get('pk')

        if not CarModel.objects.filter(pk=car_id).exists():
            return Response('Car with this id not found')

        car = CarModel.objects.get(pk=car_id)
        serializer = CarSerializer(car)
        return Response(serializer.data)
