from rest_framework.serializers import ModelSerializer

from apps.cars.serializers import CarSerializer
from apps.users.serializers import OwnerNameSerializer, OwnerSeirializer, UserSerializer

from .models import AutoParksModel


class AutoParkSerializer(ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    owners = OwnerSeirializer(many=True, read_only=True)

    # owners = UserSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'cars', 'owners')
        read_only_fields = ('owners',)
