from rest_framework.serializers import ModelSerializer

from .models import AutoSalonsModel


class AutoSalonSerializer(ModelSerializer):

    class Meta:
        model = AutoSalonsModel
        fields = ('id', 'name')
