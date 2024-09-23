from rest_framework.serializers import ModelSerializer

from apps.cars.serializers import CarSerializer

from .models import AutoSalonsModel


class AutoSalonSerializer(ModelSerializer):
    # cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoSalonsModel
        fields = ('id', 'name', 'user')
