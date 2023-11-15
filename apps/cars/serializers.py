from rest_framework.serializers import ModelSerializer
from .models import CarModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        # fields = '__all__' можна просто всі поля включити або перерахувати
        fields = ('id', 'brand', 'price', 'year')
