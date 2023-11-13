from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CarModel


# CRUD
# create
# read/retrive
# update
# delete/destroy

class CarListCreateView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        car = CarModel.objects.create(**data)

        return Response(car)
