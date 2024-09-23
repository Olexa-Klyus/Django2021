from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView

from .models import AutoSalonsModel
from .serializers import AutoSalonSerializer


class AutoSalonListCreateView(ListCreateAPIView):
    queryset = AutoSalonsModel.objects.all()
    serializer_class = AutoSalonSerializer





    # UserModel = get_user_model()
    # queryset = UserModel.objects.all()